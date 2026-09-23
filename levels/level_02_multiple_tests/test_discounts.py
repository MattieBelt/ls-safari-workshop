"""Level 2 assignment (2/2): group tests by giving them their own file.

Run just this file:
    uv run pytest levels/level_02_multiple_tests/test_discounts.py
"""

import pytest

from pricing_suite.discounts import apply_discount


def test_apply_discount_happy_path():
    assert apply_discount(total=50, percent=20) == 40


def test_apply_discount_rejects_out_of_range_percent():
    with pytest.raises(ValueError):
        apply_discount(total=50, percent=200)
