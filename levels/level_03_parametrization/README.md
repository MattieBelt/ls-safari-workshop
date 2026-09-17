# Level 3 — Test parametrization

**Goal:** replace repetitive, copy-pasted test cases with `@pytest.mark.parametrize`.

## Context

`pricing_suite/` here is a copy of level 2's package (same `calculate_total` and
`apply_discount`), kept local so this level doesn't depend on level 2's files.
`test_pricing_parametrized.py` starts with one passing test per function, one case each.
Adding a case currently means copy-pasting a whole test.

## Lesson

`@pytest.mark.parametrize` runs the same test once per input set, each reported separately:

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

Works with `pytest.raises` too — that stays inside the test body:

```python
@pytest.mark.parametrize("percent", [-1, 101, 1000])
def test_apply_discount_invalid_percent_raises(percent):
    with pytest.raises(ValueError):
        apply_discount(100, percent)
```

By default pytest names each case from its values — readable for a couple of cases, noisy
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

## Assignment

Rework the three TODOs in `test_pricing_parametrized.py`:

- [ ] `test_apply_discount_cases` — a normal discount, 0%, 100%, a total of 0
- [ ] `test_apply_discount_invalid_percent_raises` — a negative percent and one over 100
- [ ] `test_calculate_total_cases` — empty list, single item, multiple items
- [ ] Give at least one of these tests explicit `ids`

**Nice to have before moving on** — not required, but worth noticing:

- Each case is reported pass/fail on its own, unlike several asserts crammed into one test
  (which stops at the first failure and hides the rest)
- Reach for `ids` once a table gets long enough that `-v` output stops being readable

Next: [Level 4 — Fixtures](../level_04_fixtures/README.md)
