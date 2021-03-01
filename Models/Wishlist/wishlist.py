from typing import Optional
from pydantic import BaseModel



class WishlistDetails(BaseModel):

    name : str
    description : str
    categoryid : int
    no_of_votes : int
    
class WishlistEdit(WishlistDetails):

    name : Optional[str]
    description : Optional[str]
    categoryid : Optional[int]
    no_of_votes : Optional[int]
