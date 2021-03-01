from typing import Optional
from pydantic import BaseModel


class UserDetails(BaseModel):

    name: str
    email: str
    password: str
    age: Optional[int]
    mobile: Optional[int]


class UserEdit(UserDetails):

    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    age: Optional[int]
    mobile: Optional[int]
