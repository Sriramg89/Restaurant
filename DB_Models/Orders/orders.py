from ..database import *
from ..User.user import *
from ..Restaurant.restaurant import *
class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey("user.id"))
    restid = Column(Integer, ForeignKey("restaurant.id"))
    description = Column(String)
    date=Column(Date)
    cost = Column(Integer)
    user = relationship(User)
    restaurant = relationship(Restaurant)