from typing import Optional
from pydantic import BaseModel
import datetime


class ItemDetails(BaseModel):

    categid: int
    name: str
    description: str
    cost: int
    gluten_free: str
    vegetarian: str


class CategDetails(BaseModel):

    name: str
    description: str
    restid: int


class ItemEdit(ItemDetails):

    categid: Optional[int]
    name: Optional[str]
    description: Optional[str]
    cost: Optional[int]
    gluten_free: Optional[str]
    vegetarian: Optional[str]


class CategEdit(CategDetails):

    name: Optional[str]
    description: Optional[str]
    restid: Optional[int]
