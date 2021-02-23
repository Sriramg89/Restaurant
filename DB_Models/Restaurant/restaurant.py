from ..database import *
from ..User.user import *


class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    address = Column(String)
    open_time = Column(String)
    close_time = Column(String)
    rating = Column(Integer)
    average_cost = Column(Integer)
    userid = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
