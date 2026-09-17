"""Level 2 assignment (2/2): group tests by giving them their own file.

Run just this file:
    uv run pytest levels/level_02_multiple_tests/test_discounts.py
"""

import pytest

from pricing_suite.discounts import apply_discount


def test_apply_discount_happy_path():
    # TODO: apply_discount(50, 20) == 40
    raise NotImplementedError("TODO: implement this test")


def test_apply_discount_rejects_out_of_range_percent():
    # TODO: apply_discount(50, 200) raises ValueError
    raise NotImplementedError("TODO: implement this test")
