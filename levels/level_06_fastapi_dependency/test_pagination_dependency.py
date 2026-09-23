"""Level 6 assignment: unit test a FastAPI dependency directly.

Run just this file with:
    uv run pytest levels/level_06_fastapi_dependency
"""

import pytest
from fastapi import HTTPException

from app.dependencies import pagination_params


def test_pagination_params_defaults():
    assert pagination_params() == {"skip": 0, "limit": 10}


def test_pagination_params_custom_values():
    assert pagination_params(skip=5, limit=2) == {"skip": 5, "limit": 2}


@pytest.mark.parametrize("skip", [-1, -100])
def test_pagination_params_rejects_negative_skip(skip):
    with pytest.raises(HTTPException):
        pagination_params(skip=skip)


@pytest.mark.parametrize("limit", [0, -1])
def test_pagination_params_rejects_non_positive_limit(limit):
    with pytest.raises(HTTPException):
        pagination_params(limit=limit)


def test_pagination_params_error_has_400_status():
    with pytest.raises(HTTPException) as exc_info:
        pagination_params(skip=-1)

    assert exc_info.value.status_code == 400
