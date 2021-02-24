from sqlalchemy.orm import *
from sqlalchemy import *
from ..Menu.menu import *
from ..database import *
from ..User.user import *
from ..Restaurant.restaurant import *



class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey("user.id"))
    restid = Column(Integer, ForeignKey("restaurant.id"))
    description = Column(String)
    date = Column(DateTime)
    itemid = Column(Integer,ForeignKey("menu_item.id"))
    menu_item = relationship(Menu_Item)
    quantity = Column(Integer)
    # cost =Column(Integer)
    user = relationship(User)
    restaurant = relationship(Restaurant)
# Orders.cost = column_property(select(Menu_Item.cost).where(Menu_Item.id == Orders.itemid))    
