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
    # TODO: assert that apply_discount(100, 10) returns the expected value
    raise NotImplementedError("TODO: implement this test")


def test_apply_discount_zero_percent():
    # TODO: a 0% discount should return the total unchanged
    raise NotImplementedError("TODO: implement this test")


def test_apply_discount_hundred_percent():
    # TODO: a 100% discount should return 0
    raise NotImplementedError("TODO: implement this test")


def test_apply_discount_rejects_negative_percent():
    # TODO: apply_discount(100, -1) should raise ValueError
    # hint: use `with pytest.raises(ValueError):`
    raise NotImplementedError("TODO: implement this test")


def test_apply_discount_rejects_percent_over_100():
    # TODO: apply_discount(100, 101) should raise ValueError
    raise NotImplementedError("TODO: implement this test")
