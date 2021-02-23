from typing import Optional
from pydantic import BaseModel
import datetime


class OrderDetails(BaseModel):

    userid: int
    description: str
    restid: int
    cost: int
    date: datetime.date


class OrderEdit(OrderDetails):

    userid: Optional[int]
    description: Optional[str]
    restid: Optional[int]
    cost: Optional[int]
    date: Optional[datetime.date]
