"""Level 8 assignment: test HTTP routes end-to-end with TestClient.

Uses the `client` fixture from conftest.py, which wires a real TestClient to
an isolated in-memory copy of the seed data (see conftest.py for how).

Run just this file with:
    uv run pytest levels/level_08_test_client
"""


def test_list_items(client):
    # TODO: GET /items, assert status_code 200 and the response contains the
    # two seeded items (see conftest.SEED_DB)
    raise NotImplementedError("TODO: implement this test")


def test_get_item_not_found(client):
    # TODO: GET /items/999, assert status_code 404
    raise NotImplementedError("TODO: implement this test")


def test_create_item(client):
    # TODO: POST /items with json={"name": "Thingy", "price": 5.0}, assert
    # status_code 201 and the response body has the given name/price plus a
    # generated id
    raise NotImplementedError("TODO: implement this test")


def test_update_item(client):
    # TODO: PUT /items/1 with a new name/price, assert status_code 200 and
    # the response reflects the update
    raise NotImplementedError("TODO: implement this test")


def test_delete_item(client):
    # TODO: DELETE /items/1, assert status_code 204, then GET /items/1 again
    # and assert it now 404s
    raise NotImplementedError("TODO: implement this test")


def test_list_users(client):
    # TODO: GET /users, assert status_code 200 and the response contains the
    # seeded user
    raise NotImplementedError("TODO: implement this test")


def test_create_user(client):
    # TODO: POST /users with json={"name": "Alan Turing"}, assert
    # status_code 201 and the response has the given name plus a generated id
    raise NotImplementedError("TODO: implement this test")


def test_pagination_query_params_are_validated(client):
    # TODO: GET /items?skip=-1, assert status_code 400
    # (this exercises the simple `pagination_params` dependency from level 6,
    # now reached through the full HTTP stack)
    raise NotImplementedError("TODO: implement this test")


def test_create_item_rejects_invalid_price(client):
    # TODO: POST /items with json={"name": "Thingy", "price": -5.0}, assert
    # status_code 422 (this exercises ItemCreate's Field(gt=0) from level 5,
    # now reached through the full HTTP stack)
    raise NotImplementedError("TODO: implement this test")
