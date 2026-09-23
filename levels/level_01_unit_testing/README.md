# Level 1: Unit test

**Goal:** write your first pytest unit tests, against a small pure function.

## Context

`pricing.py`:

```python
def apply_discount(total: float, percent: float) -> float:
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return total - (total * percent / 100)
```

Pure function, no I/O: the simplest thing to unit test. Same function as the level 0 demo,
now with the guard clause that would've caught that bug.

## Lesson

A test is a function starting with `test_`, containing `assert`:

```python
def test_add():
    assert 1 + 1 == 2
```

Test for a raised exception with `pytest.raises`:

```python
import pytest

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

pytest also captures `print()` output, but you only see it for tests that fail, not ones that
pass. Handy to know once you start debugging a test that isn't doing what you expect.

Run: `uv run pytest levels/level_01_unit_testing`

## Assignment

Complete the TODOs in `test_apply_discount.py`:

- [ ] Happy path: `apply_discount(100, 10)` returns the expected value
- [ ] Edge case: 0% discount returns the total unchanged
- [ ] Edge case: 100% discount returns 0
- [ ] Invalid: negative percent raises `ValueError`
- [ ] Invalid: percent over 100 raises `ValueError`

Next: [Level 2: Run multiple tests](../level_02_multiple_tests/README.md)
