from fastapi import APIRouter, Depends, HTTPException

from app import store
from app.dependencies import get_db, pagination_params
from app.models import User, UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[User])
def list_users(pagination: dict = Depends(pagination_params), db: dict = Depends(get_db)):
    return store.list_users(db, **pagination)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: dict = Depends(get_db)):
    user = store.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("", response_model=User, status_code=201)
def create_user(payload: UserCreate, db: dict = Depends(get_db)):
    return store.create_user(db, payload.name)


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, payload: UserCreate, db: dict = Depends(get_db)):
    user = store.update_user(db, user_id, payload.name)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: dict = Depends(get_db)):
    if not store.delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
