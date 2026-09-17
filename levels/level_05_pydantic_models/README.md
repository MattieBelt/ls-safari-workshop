# Level 5: Pydantic models and strict typing

**Goal:** test the validation rules *you* add to a Pydantic model, not the ones Pydantic
already guarantees.

## Context

Switches from level 4's `cart.py` to the shared demo app in `app/`.

**Refresher, in case it's been a while:** a Pydantic `BaseModel` is a class with type-annotated
fields. Constructing it validates and coerces the values you pass, based on those type hints:

- Compatible types get coerced: `ItemCreate(price="9.99")` becomes `price=9.99` (a real
  float), not an error. Wildly wrong ones don't: `price="abc"` raises `ValidationError`.
- A `ValidationError` collects *every* failing field at once, not just the first, which is
  useful for building one clear error message instead of fixing input one field at a time.
- FastAPI validates request bodies through models exactly like this: a bad request never
  reaches your route function, it 422s before your code runs at all.

`app/models.py`'s `ItemCreate`:

```python
class ItemCreate(BaseModel):
    name: str
    price: float = Field(gt=0)

    @field_validator("name")
    @classmethod
    def name_must_not_include_hyphens(cls, value: str) -> str:
        value = value.strip()
        if "-" in value:
            raise ValueError("name must not include hyphens")
        return value
```

The `name` validator does two things: silently trims surrounding whitespace (normalization,
not an error), then rejects a hyphen (a real error). Worth telling apart when you write tests
for each.

Two kinds of validation live here:

- `price: float`: Pydantic's own type checking, described above.
- `Field(gt=0)` and the `name` validator: rules *we* chose. Nobody but us verifies these keep
  working.

## Lesson

Why strict models + tests together, beyond "catches bad input":

- **Validates at the boundary**: reject bad data where it enters, instead of chasing a
  confusing bug three functions deeper in
- **The model is the contract**: `ItemCreate` documents exactly what's expected; FastAPI turns
  it straight into API docs, no separate schema to maintain by hand
- **Less code to test**: once data is a validated `Item`, downstream code doesn't need
  `isinstance` checks or `None`-guards for fields that can't be missing or the wrong type; typed,
  validated data shrinks the test surface for everything after it
- **Static + runtime, together**: a type checker (mypy/pyright) catches misuse at write-time;
  Pydantic enforces the same shapes at runtime, where request bodies actually arrive and types
  can't help

Testing a model is just testing a class: construct it, see what happens:

```python
import pytest
from pydantic import ValidationError

from app.models import ItemCreate

def test_valid_item():
    item = ItemCreate(name="Widget", price=9.99)
    assert item.price == 9.99

def test_negative_price_rejected():
    with pytest.raises(ValidationError):
        ItemCreate(name="Widget", price=-5)
```

For a closer look at *why* it failed, `ValidationError.errors()` lists each failing field:

```python
def test_negative_price_error_detail():
    with pytest.raises(ValidationError) as exc_info:
        ItemCreate(name="Widget", price=-5)
    errors = exc_info.value.errors()
    assert errors[0]["loc"] == ("price",)
```

The rules this app added (`Field(gt=0)`, the `name` validator) matter most to test; nothing
else protects them. Testing Pydantic's own behavior (coercion, type rejection) isn't wrong,
it just protects against a different thing: a future Pydantic upgrade changing how it behaves,
rather than a regression in your code. Good excuse to get more parametrize practice in too
(level 3).

These rules don't only live here, either. Level 8 sends a real request through the whole app
and checks that a bad price still 422s, this time over HTTP.

## Assignment

Complete the TODOs in `test_item_model.py`:

- [ ] Valid `ItemCreate`: happy path
- [ ] A numeric string price (`"9.99"`) coerces to a float: Pydantic's own behavior, worth
      seeing once
- [ ] A few clearly invalid `price` types (e.g. `"abc"`, `None`, `[]`) all raise
      `ValidationError`; parametrize this one
- [ ] `price <= 0`: parametrize a few values (0, -1, -100), all raise `ValidationError`
- [ ] Surrounding whitespace gets trimmed: `"  Widget  "` becomes `"Widget"`
- [ ] A name containing a hyphen (e.g. `"Wid-get"`) raises `ValidationError`; parametrize a
      couple of positions (start, middle, end)
- [ ] One test that inspects `.errors()` to check *which* field failed

Next: [Level 6: Unit test a FastAPI dependency](../level_06_fastapi_dependency/README.md)
