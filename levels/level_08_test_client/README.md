# Level 8: Test routes using the FastAPI test client

**Goal:** test full HTTP routes end-to-end: request in, response out.

## Context

Levels 6 and 7 tested pieces in isolation: a dependency on its own, the data layer mocked out.
This level wires it all together: `TestClient` sends real requests through the actual app,
in-process, so routing, dependencies, and validation all run for real.

Two things worth knowing before diving in:

**`conftest.py`** is a filename pytest treats specially: any fixtures defined in it are
available to every test file in the same directory, no import needed. That's how
`test_api_routes.py` can just ask for `client` as a parameter, the same mechanism as `cart`
back in level 4, just not needing an import this time.

**`TestClient`** wraps your FastAPI app in-process: no server, no socket, no real network call.
It gives you `requests`-like methods (`.get()`, `.post()`, ...) that run a request straight
through the app and hand back a real response.

This level's `client` fixture, in `conftest.py`, builds on both: it hands you a `TestClient`,
wired so tests still don't touch `app/data/db.json`. Two tools make that possible:

- **`dependency_overrides`** (new): swaps `get_db` for a function returning an isolated,
  in-memory copy of seed data
- **`monkeypatch`** (level 7): neutralizes `store.write_db`, since the CRUD functions call it
  directly rather than through a dependency

Read `conftest.py` before starting; no fixtures to write this level, only tests.

## Lesson

```python
def test_list_items(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 2
```

`app.dependency_overrides` is a dict keyed by the dependency function:

```python
app.dependency_overrides[get_db] = fake_get_db
...
app.dependency_overrides.clear()  # always clean up
```

Learn more on your own: [FastAPI's testing guide](https://fastapi.tiangolo.com/tutorial/testing/)
and [pytest's docs on fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) (the
`conftest.py` section covers sharing them across files).

## Assignment

Complete the TODOs in `test_api_routes.py`:

- [ ] `GET /items` → 200, seeded items
- [ ] `GET /items/{id}` missing → 404
- [ ] `POST /items` → 201, generated id
- [ ] `PUT /items/{id}` → 200, updated values
- [ ] `DELETE /items/{id}` → 204, then 404 on re-fetch
- [ ] `GET /users` → 200, seeded user
- [ ] `POST /users` → 201
- [ ] `GET /items?skip=-1` → 400 (level 6's dependency, now over HTTP)
- [ ] `POST /items` with a negative price → 422 (level 5's validation, now over HTTP)

That's the workshop. From level 0's one risky function to here: a typed, validated,
dependency-injected API tested at every layer: unit, mocked, and now full HTTP.
`app/data/db.json` should still be untouched.
