from typing import Optional
from pydantic import BaseModel
import datetime


class InventoryDetails(BaseModel):

    name : str
    quantity : int
    itemid : int
    restaurantid : int
    
    
class InventoryEdit(InventoryDetails):

    name : Optional[str]
    quantity : Optional[int]
    restaurantid : Optional[int]
    itemid : Optional[int]