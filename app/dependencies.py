"""The app's two example dependencies.

- ``pagination_params`` is the *simple* dependency: pure, no I/O, easy to call
  directly in a unit test.
- ``get_db`` is the *complex* dependency: it hits disk (our "noSQL" file) on
  every call, so testing code that depends on it usually means mocking it out.
"""

from fastapi import HTTPException

from app.store import read_db


def pagination_params(skip: int = 0, limit: int = 10) -> dict:
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip must be >= 0")
    if limit <= 0:
        raise HTTPException(status_code=400, detail="limit must be > 0")
    return {"skip": skip, "limit": limit}


def get_db() -> dict:
    return read_db()
