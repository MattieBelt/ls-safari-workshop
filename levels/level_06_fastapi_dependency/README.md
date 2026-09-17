# Level 6 — Unit test a FastAPI dependency

**Goal:** test a FastAPI dependency the same way you'd test any function — because that's what
it is.

## Context

Same `app/` as level 5, now testing `app/dependencies.py`:

```python
def pagination_params(skip: int = 0, limit: int = 10) -> dict:
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip must be >= 0")
    if limit <= 0:
        raise HTTPException(status_code=400, detail="limit must be > 0")
    return {"skip": skip, "limit": limit}
```

**Refresher, in case it's been a while:** a route declares a dependency with a `Depends(...)`
default:

```python
@router.get("/items")
def list_items(pagination: dict = Depends(pagination_params), db: dict = Depends(get_db)):
    return store.list_items(db, **pagination)
```

Before calling `list_items`, FastAPI calls `pagination_params()` itself — binding `skip`/`limit`
from the request's query params the same way it would for a route — and passes whatever it
returns in as `pagination`. That's it; there's no base class, no registration, no magic.
`pagination_params` has no idea FastAPI is involved. It's a plain function, called by another
piece of code, the same as any function call.

## Lesson

That's exactly why it's testable on its own: nothing about it depends on a request, a
response, or a running server, so nothing about *testing* it needs one either.

- **Fast** — a plain function call, no ASGI app or test client to spin up
- **Isolated** — a failure here means pagination logic is wrong, not routing, not the
  database, not some other dependency it happens to sit next to
- **Tested once, trusted everywhere** — `pagination_params` backs both `/items` and `/users`;
  testing it directly covers every route that uses it, instead of re-proving the same logic
  once per route

Not every dependency is this easy, though — `get_db` (level 7) hits the filesystem every call,
which is a different kind of problem. And eventually you do want to know the whole stack works
together, wiring included — that's level 8. Different levels of confidence, at different costs;
a real app leans on all three.

Import and call it directly:

```python
from app.dependencies import pagination_params

def test_defaults():
    assert pagination_params() == {"skip": 0, "limit": 10}
```

`HTTPException` is a normal exception — assert it like any other:

```python
import pytest
from fastapi import HTTPException

def test_rejects_negative_skip():
    with pytest.raises(HTTPException):
        pagination_params(skip=-1)
```

Catching the exception type is a start — inspecting it is better, same as `.errors()` in level 5:

```python
def test_rejects_negative_skip_with_400():
    with pytest.raises(HTTPException) as exc_info:
        pagination_params(skip=-1)
    assert exc_info.value.status_code == 400
```

## Assignment

Complete the TODOs in `test_pagination_dependency.py`:

- [ ] Defaults: `pagination_params()` returns `{"skip": 0, "limit": 10}`
- [ ] Custom values: `pagination_params(skip=5, limit=2)` returns them unchanged
- [ ] Invalid: negative `skip` raises `HTTPException` — parametrize a couple of values
- [ ] Invalid: non-positive `limit` raises `HTTPException` — parametrize a couple of values
- [ ] One test that inspects the exception — assert `status_code == 400`

Next: [Level 7 — Mock a sub dependency](../level_07_mocking/README.md)
