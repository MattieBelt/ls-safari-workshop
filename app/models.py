from pydantic import BaseModel, Field, field_validator


class ItemCreate(BaseModel):
    name: str
    price: float = Field(gt=0)

    @field_validator("name")
    @classmethod
    def name_must_not_include_hyphens(cls, value: str) -> str:
        value = value.strip()
        if "-" in value:
            raise ValueError("name must not include hyphens")
        return value


class Item(ItemCreate):
    id: int


class UserCreate(BaseModel):
    name: str


class User(UserCreate):
    id: int
