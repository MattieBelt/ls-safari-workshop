from fastapi import APIRouter, Depends, HTTPException

from app import store
from app.dependencies import get_db, pagination_params
from app.models import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[Item])
def list_items(pagination: dict = Depends(pagination_params), db: dict = Depends(get_db)):
    return store.list_items(db, **pagination)


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, db: dict = Depends(get_db)):
    item = store.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("", response_model=Item, status_code=201)
def create_item(payload: ItemCreate, db: dict = Depends(get_db)):
    return store.create_item(db, payload.name, payload.price)


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate, db: dict = Depends(get_db)):
    item = store.update_item(db, item_id, payload.name, payload.price)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: dict = Depends(get_db)):
    if not store.delete_item(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
