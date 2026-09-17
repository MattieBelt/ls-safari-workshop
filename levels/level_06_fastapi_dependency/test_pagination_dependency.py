"""Level 6 assignment: unit test a FastAPI dependency directly.

Run just this file with:
    uv run pytest levels/level_06_fastapi_dependency
"""

import pytest
from fastapi import HTTPException

from app.dependencies import pagination_params


def test_pagination_params_defaults():
    # TODO: calling pagination_params() with no args should return
    # {"skip": 0, "limit": 10}
    raise NotImplementedError("TODO: implement this test")


def test_pagination_params_custom_values():
    # TODO: pagination_params(skip=5, limit=2) should return
    # {"skip": 5, "limit": 2}
    raise NotImplementedError("TODO: implement this test")


@pytest.mark.parametrize("skip", [-1, -100])
def test_pagination_params_rejects_negative_skip(skip):
    # TODO: pagination_params(skip=skip) should raise HTTPException
    # hint: use `with pytest.raises(HTTPException):`
    raise NotImplementedError("TODO: implement this test")


@pytest.mark.parametrize("limit", [0, -1])
def test_pagination_params_rejects_non_positive_limit(limit):
    # TODO: pagination_params(limit=limit) should raise HTTPException
    raise NotImplementedError("TODO: implement this test")


def test_pagination_params_error_has_400_status():
    # TODO: catch the HTTPException from a negative skip, then assert
    # exc_info.value.status_code == 400
    raise NotImplementedError("TODO: implement this test")
