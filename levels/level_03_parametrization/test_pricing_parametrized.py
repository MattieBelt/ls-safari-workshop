"""Level 3 assignment: replace repetitive tests with parametrization.

Reuses the pricing_suite package from level 2
(levels/level_02_multiple_tests/pricing_suite/) instead of its own copy.

Run just this file with:
    uv run pytest levels/level_03_parametrization -v
"""

import pytest

from pricing_suite.basket import calculate_total
from pricing_suite.discounts import apply_discount


@pytest.mark.parametrize(
    "total, percent, expected",
    [
        pytest.param(100, 10, 90, id="ten_percent"),
        pytest.param(100, 0, 100, id="zero_percent"),
        pytest.param(100, 100, 0, id="hundred_percent"),
        pytest.param(0, 50, 0, id="zero_total"),
    ],
)
def test_apply_discount_cases(total, percent, expected):
    assert apply_discount(total=total, percent=percent) == expected


@pytest.mark.parametrize("percent", [-1, 101])
def test_apply_discount_invalid_percent_raises(percent):
    with pytest.raises(ValueError):
        apply_discount(total=100, percent=percent)


@pytest.mark.parametrize(
    "prices, expected",
    [
        pytest.param([], 0, id="empty"),
        pytest.param([5.0], 5.0, id="single_item"),
        pytest.param([1.0, 2.0, 3.0], 6.0, id="multiple_items"),
    ],
)
def test_calculate_total_cases(prices, expected):
    assert calculate_total(prices=prices) == expected
