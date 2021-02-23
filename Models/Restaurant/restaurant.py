from typing import Optional
from pydantic import BaseModel
import datetime

class RestDetails(BaseModel):

    name: str
    address: str
    open_time: datetime.time
    close_time: datetime.time
    userid: int
    rating: int
    average_cost: int

class RestEdit(RestDetails):

    name: Optional[str]
    address: Optional[str]
    open_time: Optional[datetime.time]
    close_time: Optional[datetime.time]
    userid: Optional[int]
    rating: Optional[int]
    average_cost: Optional[int]