"""Level 5 assignment: test the validation rules added on top of Pydantic.

Run just this file with:
    uv run pytest levels/level_05_pydantic_models
"""

import pytest
from pydantic import ValidationError

from app.models import ItemCreate


def test_valid_item():
    # TODO: ItemCreate(name="Widget", price=9.99) constructs fine;
    # assert item.name == "Widget" and item.price == 9.99
    raise NotImplementedError("TODO: implement this test")


def test_numeric_string_price_coerces_to_float():
    # TODO: ItemCreate(name="Widget", price="9.99").price should be the float
    # 9.99, not the string "9.99" - Pydantic's own coercion, not ours
    raise NotImplementedError("TODO: implement this test")


@pytest.mark.parametrize("price", ["abc", None, []])
def test_invalid_price_type_rejected(price):
    # TODO: ItemCreate(name="Widget", price=price) should raise ValidationError
    raise NotImplementedError("TODO: implement this test")


@pytest.mark.parametrize("price", [0, -1, -100])
def test_non_positive_price_rejected(price):
    # TODO: ItemCreate(name="Widget", price=price) should raise ValidationError
    raise NotImplementedError("TODO: implement this test")


def test_name_whitespace_is_trimmed():
    # TODO: ItemCreate(name="  Widget  ", price=9.99).name == "Widget"
    raise NotImplementedError("TODO: implement this test")


@pytest.mark.parametrize("name", ["-Widget", "Wid-get", "Widget-"])
def test_name_with_hyphen_rejected(name):
    # TODO: ItemCreate(name=name, price=9.99) should raise ValidationError
    raise NotImplementedError("TODO: implement this test")


def test_validation_error_reports_the_failing_field():
    # TODO: catch the ValidationError from a negative price, then assert
    # exc_info.value.errors()[0]["loc"] == ("price",)
    raise NotImplementedError("TODO: implement this test")
