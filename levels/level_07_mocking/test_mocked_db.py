"""Level 7 assignment: mock the "sub dependency" that does file I/O.

Run just this file with:
    uv run pytest levels/level_07_mocking
"""

from unittest.mock import Mock

import app.dependencies as dependencies
import app.store as store


def test_get_db_returns_whatever_read_db_returns(monkeypatch):
    fake_data = {"items": [], "users": []}
    monkeypatch.setattr(dependencies, "read_db", Mock(return_value=fake_data))

    assert dependencies.get_db() == fake_data


def test_create_item_persists_via_write_db(monkeypatch):
    fake_write_db = Mock()
    monkeypatch.setattr(store, "write_db", fake_write_db)
    db = {"items": [], "users": []}

    item = store.create_item(db=db, name="Widget", price=1.0)

    assert item["name"] == "Widget"
    assert item["price"] == 1.0
    assert item["id"] == 1
    fake_write_db.assert_called_once()


def test_delete_item_does_not_write_when_item_missing(monkeypatch):
    fake_write_db = Mock()
    monkeypatch.setattr(store, "write_db", fake_write_db)
    db = {"items": [], "users": []}

    result = store.delete_item(db=db, item_id=999)

    assert result is False
    fake_write_db.assert_not_called()


def test_delete_item_writes_when_item_exists(monkeypatch):
    fake_write_db = Mock()
    monkeypatch.setattr(store, "write_db", fake_write_db)
    db = {"items": [{"id": 1, "name": "Widget", "price": 1.0}], "users": []}

    result = store.delete_item(db=db, item_id=1)

    assert result is True
    fake_write_db.assert_called_once()


def test_update_item_persists_via_write_db(monkeypatch):
    fake_write_db = Mock()
    monkeypatch.setattr(store, "write_db", fake_write_db)
    db = {"items": [{"id": 1, "name": "Widget", "price": 1.0}], "users": []}

    item = store.update_item(db=db, item_id=1, name="New Name", price=2.0)

    assert item["name"] == "New Name"
    assert item["price"] == 2.0
    fake_write_db.assert_called_once()
