"""Level 5 assignment: test the validation rules added on top of Pydantic.

Run just this file with:
    uv run pytest levels/level_05_pydantic_models
"""

import pytest
from pydantic import ValidationError

from app.models import ItemCreate


def test_valid_item():
    item = ItemCreate(name="Widget", price=9.99)

    assert item.name == "Widget"
    assert item.price == 9.99


def test_numeric_string_price_coerces_to_float():
    item = ItemCreate(name="Widget", price="9.99")

    assert item.price == 9.99
    assert isinstance(item.price, float)


@pytest.mark.parametrize("price", ["abc", None, []])
def test_invalid_price_type_rejected(price):
    with pytest.raises(ValidationError):
        ItemCreate(name="Widget", price=price)


@pytest.mark.parametrize("price", [0, -1, -100])
def test_non_positive_price_rejected(price):
    with pytest.raises(ValidationError):
        ItemCreate(name="Widget", price=price)


def test_name_whitespace_is_trimmed():
    item = ItemCreate(name="  Widget  ", price=9.99)

    assert item.name == "Widget"


@pytest.mark.parametrize("name", ["-Widget", "Wid-get", "Widget-"])
def test_name_with_hyphen_rejected(name):
    with pytest.raises(ValidationError):
        ItemCreate(name=name, price=9.99)


def test_validation_error_reports_the_failing_field():
    with pytest.raises(ValidationError) as exc_info:
        ItemCreate(name="Widget", price=-5)

    errors = exc_info.value.errors()
    assert errors[0]["loc"] == ("price",)
