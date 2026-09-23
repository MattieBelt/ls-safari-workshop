"""Level 1 assignment: write your first unit tests.

Run just this file with:
    uv run pytest levels/level_01_unit_testing

Note: every level's assignment file has a unique name (test_apply_discount.py,
test_pricing_suite.py, ...) on purpose - pytest can't collect two files with the
same module name unless they're in packages, so keep that pattern in later levels.
"""

import pytest

from pricing import apply_discount


def test_apply_discount_happy_path():
    assert apply_discount(total=100, percent=10) == 90


def test_apply_discount_zero_percent():
    assert apply_discount(total=100, percent=0) == 100


def test_apply_discount_hundred_percent():
    assert apply_discount(total=100, percent=100) == 0


def test_apply_discount_rejects_negative_percent():
    with pytest.raises(ValueError):
        apply_discount(total=100, percent=-1)


def test_apply_discount_rejects_percent_over_100():
    with pytest.raises(ValueError):
        apply_discount(total=100, percent=101)
