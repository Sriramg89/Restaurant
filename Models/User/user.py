from typing import Optional
from pydantic import BaseModel
import datetime


class UserDetails(BaseModel):

    name: str
    email: str
    password: str
    age: int
    mobile: int


class UserEdit(UserDetails):

    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    age: Optional[int]
    mobile: Optional[int]
