# Level 3: Test parametrization

**Goal:** replace repetitive, copy-pasted test cases with `@pytest.mark.parametrize`.

## Context

`pricing_suite/` here is a copy of level 2's package (same `calculate_total` and
`apply_discount`), kept local so this level doesn't depend on level 2's files.
`test_pricing_parametrized.py` starts with one passing test per function, one case each.
Adding a case currently means copy-pasting a whole test.

## Lesson

In order to run the same test for multiple input sets we can use the `@pytest.mark.parametrize` decorator to set-up the testing data that will be used in the test function:

```python
import pytest

@pytest.mark.parametrize(
    "total, percent, expected",
    [
        (100, 10, 90),
        (100, 0, 100),
        (100, 100, 0),
        (0, 50, 0),
    ],
)
def test_apply_discount_cases(total, percent, expected):
    assert apply_discount(total, percent) == expected
```

It works with `pytest.raises` too, which stays inside the test body:

```python
@pytest.mark.parametrize("percent", [-1, 101, 1000])
def test_apply_discount_invalid_percent_raises(percent):
    with pytest.raises(ValueError):
        apply_discount(100, percent)
```

By default pytest names each case from its values: readable for a couple of cases, noisy
once the table grows (`test_apply_discount_cases[100-10-90]`). Give cases explicit names with
`ids`:

```python
@pytest.mark.parametrize(
    "total, percent, expected",
    [
        (100, 10, 90),
        (100, 0, 100),
        (100, 100, 0),
    ],
    ids=["ten_percent", "zero_percent", "hundred_percent"],
)
def test_apply_discount_cases(total, percent, expected):
    assert apply_discount(total, percent) == expected
```

Now `-v` shows `test_apply_discount_cases[zero_percent]` instead of a wall of numbers.

A separate `ids` list works, but it's easy for it to drift out of sync once you add or reorder cases.
The id and the values it belongs to live in two different places. `pytest.param()` keeps them together, one id right next to its own row:

```python
@pytest.mark.parametrize(
    "total, percent, expected",
    [
        pytest.param(100, 10, 90, id="ten_percent"),
        pytest.param(100, 0, 100, id="zero_percent"),
        pytest.param(100, 100, 0, id="hundred_percent"),
    ],
)
def test_apply_discount_cases(total, percent, expected):
    assert apply_discount(total, percent) == expected
```

Same result as the `ids=` list above. But `pytest.param()` is preferred once a table has more than a handful of cases.

## Assignment

Rework the three TODOs in `test_pricing_parametrized.py`:

- [ ] `test_apply_discount_cases`: a normal discount, 0%, 100%, a total of 0
- [ ] `test_apply_discount_invalid_percent_raises`: a negative percent and one over 100
- [ ] `test_calculate_total_cases`: empty list, single item, multiple items
- [ ] Give at least one of these tests explicit ids (`ids=` or `pytest.param(..., id=...)`)

**Nice to have before moving on.** Not required, but worth noticing:

- Each case is reported pass/fail on its own, unlike several asserts crammed into one test
  (which stops at the first failure and hides the rest)
- Reach for `ids` once a table gets long enough that `-v` output stops being readable

Next: [Level 4: Fixtures](../level_04_fixtures/README.md)
