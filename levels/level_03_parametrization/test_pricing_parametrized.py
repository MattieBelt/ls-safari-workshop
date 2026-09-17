"""Level 3 assignment: replace repetitive tests with parametrization.

Reuses the pricing_suite package from level 2
(levels/level_02_multiple_tests/pricing_suite/) instead of its own copy.

Run just this file with:
    uv run pytest levels/level_03_parametrization -v
"""

import pytest

from pricing_suite.basket import calculate_total
from pricing_suite.discounts import apply_discount

# TODO: replace this single case with @pytest.mark.parametrize covering at
# least: a normal discount, 0%, 100%, and a total of 0.
def test_apply_discount_cases():
    assert apply_discount(100, 10) == 90


# TODO: turn this into a parametrized test with pytest.raises inside the test
# body, covering both a negative percent and a percent over 100.
def test_apply_discount_invalid_percent_raises():
    with pytest.raises(ValueError):
        apply_discount(100, -1)


# TODO: parametrize calculate_total over a handful of price lists, including
# an empty list and a list with a single item.
def test_calculate_total_cases():
    assert calculate_total([1.0, 2.0, 3.0]) == 6.0
