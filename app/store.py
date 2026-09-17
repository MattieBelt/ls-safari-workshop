"""The "noSQL" data layer: a JSON file on disk, read and written in full each time.

Kept deliberately simple (a file, not a real database) so the workshop can focus on
*how* to test code that depends on I/O, not on database setup.
"""

import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "db.json"


def read_db() -> dict:
    with DB_PATH.open("r") as f:
        return json.load(f)


def write_db(data: dict) -> None:
    with DB_PATH.open("w") as f:
        json.dump(data, f, indent=2)


def _next_id(records: list[dict]) -> int:
    return max((r["id"] for r in records), default=0) + 1


def list_items(db: dict, skip: int = 0, limit: int = 10) -> list[dict]:
    return db["items"][skip : skip + limit]


def get_item(db: dict, item_id: int) -> dict | None:
    return next((i for i in db["items"] if i["id"] == item_id), None)


def create_item(db: dict, name: str, price: float) -> dict:
    item = {"id": _next_id(db["items"]), "name": name, "price": price}
    db["items"].append(item)
    write_db(db)
    return item


def update_item(db: dict, item_id: int, name: str, price: float) -> dict | None:
    item = get_item(db, item_id)
    if item is None:
        return None
    item["name"] = name
    item["price"] = price
    write_db(db)
    return item


def delete_item(db: dict, item_id: int) -> bool:
    item = get_item(db, item_id)
    if item is None:
        return False
    db["items"].remove(item)
    write_db(db)
    return True


def list_users(db: dict, skip: int = 0, limit: int = 10) -> list[dict]:
    return db["users"][skip : skip + limit]


def get_user(db: dict, user_id: int) -> dict | None:
    return next((u for u in db["users"] if u["id"] == user_id), None)


def create_user(db: dict, name: str) -> dict:
    user = {"id": _next_id(db["users"]), "name": name}
    db["users"].append(user)
    write_db(db)
    return user


def update_user(db: dict, user_id: int, name: str) -> dict | None:
    user = get_user(db, user_id)
    if user is None:
        return None
    user["name"] = name
    write_db(db)
    return user


def delete_user(db: dict, user_id: int) -> bool:
    user = get_user(db, user_id)
    if user is None:
        return False
    db["users"].remove(user)
    write_db(db)
    return True
