"""Level 4 assignment: extract repeated setup into fixtures.

Run just this file with:
    uv run pytest levels/level_04_fixtures
"""

import pytest

from cart import Cart


@pytest.fixture
def cart():
    return Cart()


def test_empty_cart_totals_zero(cart):
    assert cart.total() == 0


def test_add_increases_total(cart):
    cart.add(price=10)

    assert cart.total() == 10


@pytest.fixture
def full_cart(cart):
    cart.add(price=10)
    cart.add(price=20)
    return cart


def test_full_cart_total(full_cart):
    assert full_cart.total() == 30
