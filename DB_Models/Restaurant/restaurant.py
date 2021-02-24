
from ..database import *
from ..User.user import *
from sqlalchemy import Time


class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    address = Column(String)
    open_time = Column(Time)
    close_time = Column(Time)
    rating = Column(Integer)
    average_cost = Column(Integer)
    userid = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
