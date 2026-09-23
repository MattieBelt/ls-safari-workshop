"""Level 8 assignment: test HTTP routes end-to-end with TestClient.

Uses the `client` fixture from conftest.py, which wires a real TestClient to
an isolated in-memory copy of the seed data (see conftest.py for how).

Run just this file with:
    uv run pytest levels/level_08_test_client
"""


def test_list_items(client):
    response = client.get("/items")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_item_not_found(client):
    response = client.get("/items/999")

    assert response.status_code == 404


def test_create_item(client):
    response = client.post("/items", json={"name": "Thingy", "price": 5.0})

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Thingy"
    assert body["price"] == 5.0
    assert "id" in body


def test_update_item(client):
    response = client.put("/items/1", json={"name": "Updated", "price": 1.23})

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Updated"
    assert body["price"] == 1.23


def test_delete_item(client):
    response = client.delete("/items/1")
    assert response.status_code == 204

    response = client.get("/items/1")
    assert response.status_code == 404


def test_list_users(client):
    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_user(client):
    response = client.post("/users", json={"name": "Alan Turing"})

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Alan Turing"
    assert "id" in body


def test_pagination_query_params_are_validated(client):
    response = client.get("/items?skip=-1")

    assert response.status_code == 400


def test_create_item_rejects_invalid_price(client):
    response = client.post("/items", json={"name": "Thingy", "price": -5.0})

    assert response.status_code == 422
