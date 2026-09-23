"""Level 2 assignment (1/2): group tests with classes.

Run just this file:
    uv run pytest levels/level_02_multiple_tests/test_basket.py
"""

import pytest

from pricing_suite.basket import add_item, calculate_total


class TestCalculateTotal:
    def test_calculate_total_sums_prices(self):
        assert calculate_total(prices=[1.0, 2.0, 3.0]) == 6.0

    def test_calculate_total_empty_list_is_zero(self):
        assert calculate_total(prices=[]) == 0


class TestAddItem:
    def test_add_item_appends_price(self):
        assert add_item(prices=[1.0, 2.0], price=3.0) == [1.0, 2.0, 3.0]

    def test_add_item_rejects_negative_price(self):
        with pytest.raises(ValueError):
            add_item(prices=[1.0], price=-5.0)
