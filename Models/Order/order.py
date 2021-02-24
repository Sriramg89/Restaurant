from typing import Optional
from pydantic import BaseModel
import datetime


class OrderDetails(BaseModel):

    userid: int
    description: str
    restid: int
    date: datetime.date
    quantity: int
    itemid: int


class OrderEdit(OrderDetails):

    userid: Optional[int]
    description: Optional[str]
    restid: Optional[int]
    date: Optional[datetime.date]
    quantity: Optional[int]
    itemid: Optional[int]
