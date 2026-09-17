# Level 4 — Fixtures

**Goal:** stop repeating setup code in every test — extract it into a fixture.

## Context

`cart.py`:

```python
class Cart:
    def __init__(self):
        self.items: list[float] = []

    def add(self, price: float) -> None:
        self.items.append(price)

    def total(self) -> float:
        return sum(self.items)
```

First stateful example so far — every test needs its own fresh `Cart()`. Without a fixture
that's `cart = Cart()` copy-pasted at the top of each test.

## Lesson

A fixture is a function decorated with `@pytest.fixture`. A test asks for it by naming it as a
parameter — pytest calls the fixture and hands over the result:

```python
@pytest.fixture
def cart():
    return Cart()

def test_add_increases_total(cart):
    cart.add(10)
    assert cart.total() == 10
```

Fresh `Cart()` per test by default — no state leaks between tests.

Fixtures can set up *and* tear down, using `yield` instead of `return`:

```python
@pytest.fixture
def cart():
    cart = Cart()
    yield cart
    cart.items.clear()  # runs after the test, even if it failed
```

`Cart` doesn't need this — nothing to clean up. `get_db` (level 7) does: teardown is how you'd
reset it after a test writes to it.

Fixtures can depend on other fixtures too — request one as a parameter of another:

```python
@pytest.fixture
def full_cart(cart):
    cart.add(10)
    cart.add(20)
    return cart
```

## Assignment

Complete the TODOs in `test_cart.py`:

- [ ] `cart` fixture — returns a fresh `Cart()`
- [ ] Test: an empty cart totals 0
- [ ] Test: adding items increases the total
- [ ] `full_cart` fixture — depends on `cart`, pre-adds a couple of items
- [ ] Test: `full_cart`'s total matches what you added

**Nice to have before moving on** — not required, but worth noticing:

- `monkeypatch` (level 7) and the `client` fixture (level 8, already in that level's
  `conftest.py`) are both just fixtures — same mechanism you just used
- Fixtures default to function scope (one fresh instance per test); `scope="module"` or
  `"session"` shares one instance across many tests instead — faster for expensive setup, but
  tests then aren't isolated from each other

Next: [Level 5 — Pydantic models and strict typing](../level_05_pydantic_models/README.md)
