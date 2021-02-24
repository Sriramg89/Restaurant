from DB_Models.Menu.menu import *
from ..database import *
from ..Restaurant.restaurant import *


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    itemid = Column(Integer, ForeignKey("menu_item.id"))
    restaurantid = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)
    menu_item = relationship(Menu_Item)
