# Level 7 — Mock a sub dependency

**Goal:** test code that depends on disk I/O without touching the real file.

## Context

This is the dependency level 6 flagged as "a different kind of problem." `app.dependencies.get_db`
reads `app/data/db.json` off disk on every call:

```python
def get_db() -> dict:
    return read_db()
```

`app/store.py` writes back to that file after every create/update/delete. Calling these
directly in a test means reading/writing a real file every run — slow, and one crashed write
corrupts data for every test after it.

Fix: replace (mock) `read_db`/`write_db` with a stand-in that doesn't touch disk. The same
move applies to anything else a test shouldn't do for real: calling an external API, sending
an email, or depending on something non-deterministic like `datetime.now()`.

## Lesson

`monkeypatch` — the fixture level 4 promised you'd meet again — swaps an attribute for the
test, restores it after:

```python
def test_example(monkeypatch):
    monkeypatch.setattr(dependencies, "read_db", lambda: {"items": [], "users": []})
    assert dependencies.get_db() == {"items": [], "users": []}
```

`unittest.mock.Mock` records how it was called, so you can assert on that:

```python
from unittest.mock import Mock

def test_write_is_called(monkeypatch):
    fake_write = Mock()
    monkeypatch.setattr(store, "write_db", fake_write)
    store.create_item({"items": [], "users": []}, name="Widget", price=1.0)
    fake_write.assert_called_once()
    # or check what it was called with, not just that it was called:
    fake_write.assert_called_once_with({"items": [{"id": 1, "name": "Widget", "price": 1.0}], "users": []})
```

## Assignment

Complete the TODOs in `test_mocked_db.py`:

- [ ] `get_db` returns exactly what the (mocked) `read_db` returns
- [ ] `create_item` calls `write_db` once, returns a correctly-built item
- [ ] `delete_item` on a missing id returns `False`, does **not** call `write_db`
- [ ] `delete_item` on an existing id returns `True`, calls `write_db` once
- [ ] `update_item` on an existing id calls `write_db` once, returns the updated item

Check `app/data/db.json` is unchanged after running.

Next: [Level 8 — Test routes with the test client](../level_08_test_client/README.md)
