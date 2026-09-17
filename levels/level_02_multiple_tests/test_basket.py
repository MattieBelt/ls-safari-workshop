"""Level 2 assignment (1/2): group tests with classes.

Run just this file:
    uv run pytest levels/level_02_multiple_tests/test_basket.py
"""

from pricing_suite.basket import add_item, calculate_total


class TestCalculateTotal:
    def test_calculate_total_sums_prices(self):
        # TODO: calculate_total([1.0, 2.0, 3.0]) == 6.0
        raise NotImplementedError("TODO: implement this test")

    def test_calculate_total_empty_list_is_zero(self):
        # TODO: calculate_total([]) == 0
        raise NotImplementedError("TODO: implement this test")


class TestAddItem:
    def test_add_item_appends_price(self):
        # TODO: add_item([1.0, 2.0], 3.0) == [1.0, 2.0, 3.0]
        raise NotImplementedError("TODO: implement this test")

    def test_add_item_rejects_negative_price(self):
        # TODO: add_item([1.0], -5.0) raises ValueError
        raise NotImplementedError("TODO: implement this test")
