"""Shared fixture for level 8: a TestClient wired to an isolated, in-memory db.

Provided as infrastructure (like app/ itself) so the assignment can focus on
writing route tests, not on fixture plumbing. Read it anyway - the pattern
(dependency_overrides + monkeypatch) is the actual lesson.
"""

import copy

import pytest
from fastapi.testclient import TestClient

from app.dependencies import get_db
from app.main import app

SEED_DB = {
    "items": [
        {"id": 1, "name": "Widget", "price": 9.99},
        {"id": 2, "name": "Gadget", "price": 19.99},
    ],
    "users": [
        {"id": 1, "name": "Ada Lovelace"},
    ],
}


@pytest.fixture
def client(monkeypatch):
    test_db = copy.deepcopy(SEED_DB)

    def fake_get_db():
        return test_db

    # store.create_item/update_item/delete_item always call store.write_db()
    # directly (not via a dependency), so it must be neutralized separately
    # from the get_db override above - otherwise tests would still write to
    # the real app/data/db.json.
    monkeypatch.setattr("app.store.write_db", lambda data: None)

    app.dependency_overrides[get_db] = fake_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
