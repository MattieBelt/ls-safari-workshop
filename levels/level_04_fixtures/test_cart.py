"""Level 4 assignment: extract repeated setup into fixtures.

Run just this file with:
    uv run pytest levels/level_04_fixtures
"""

import pytest

from cart import Cart


@pytest.fixture
def cart():
    # TODO: return a fresh Cart()
    raise NotImplementedError("TODO: implement this fixture")


def test_empty_cart_totals_zero(cart):
    # TODO: assert a fresh cart totals 0
    raise NotImplementedError("TODO: implement this test")


def test_add_increases_total(cart):
    # TODO: cart.add(10), then assert cart.total() == 10
    raise NotImplementedError("TODO: implement this test")


@pytest.fixture
def full_cart(cart):
    # TODO: add a couple of items to `cart` (e.g. 10 and 20), then return it
    raise NotImplementedError("TODO: implement this fixture")


def test_full_cart_total(full_cart):
    # TODO: assert full_cart.total() equals the sum of what you added above
    raise NotImplementedError("TODO: implement this test")
