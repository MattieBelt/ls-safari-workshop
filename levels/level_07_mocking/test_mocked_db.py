"""Level 7 assignment: mock the "sub dependency" that does file I/O.

Run just this file with:
    uv run pytest levels/level_07_mocking
"""

from unittest.mock import Mock

import app.dependencies as dependencies
import app.store as store


def test_get_db_returns_whatever_read_db_returns(monkeypatch):
    fake_data = {"items": [], "users": []}
    # TODO: use monkeypatch.setattr to replace dependencies.read_db with a
    # Mock(return_value=fake_data), then assert dependencies.get_db() returns
    # fake_data exactly (proving get_db never touches the real db.json here).
    raise NotImplementedError("TODO: implement this test")


def test_create_item_persists_via_write_db(monkeypatch):
    fake_write_db = Mock()
    # TODO: use monkeypatch.setattr to replace store.write_db with
    # fake_write_db, then call store.create_item on an in-memory db dict
    # (e.g. {"items": [], "users": []}) and assert:
    #   - the returned item has the right name/price and a generated id
    #   - fake_write_db was called exactly once (fake_write_db.assert_called_once())
    raise NotImplementedError("TODO: implement this test")


def test_delete_item_does_not_write_when_item_missing(monkeypatch):
    fake_write_db = Mock()
    # TODO: replace store.write_db with fake_write_db, call
    # store.delete_item(db, item_id=999) on a db with no such item, assert it
    # returns False, and assert fake_write_db was NOT called
    # (fake_write_db.assert_not_called()).
    raise NotImplementedError("TODO: implement this test")


def test_delete_item_writes_when_item_exists(monkeypatch):
    fake_write_db = Mock()
    # TODO: replace store.write_db with fake_write_db, call
    # store.delete_item(db, item_id=1) on a db that HAS that item, assert it
    # returns True, and assert fake_write_db was called once.
    raise NotImplementedError("TODO: implement this test")


def test_update_item_persists_via_write_db(monkeypatch):
    fake_write_db = Mock()
    # TODO: replace store.write_db with fake_write_db, call
    # store.update_item(db, item_id=1, name="New Name", price=2.0) on a db
    # that has that item, and assert:
    #   - the returned item has the new name/price
    #   - fake_write_db was called once
    raise NotImplementedError("TODO: implement this test")
