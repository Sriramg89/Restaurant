from typing import Optional
from pydantic import BaseModel


class WishlistDetails(BaseModel):

    name: str
    description: str
    menu_category: str
    no_of_votes: int


class WishlistEdit(WishlistDetails):

    name: Optional[str]
    description: Optional[str]
    menu_category: Optional[str]
    no_of_votes: Optional[int]
