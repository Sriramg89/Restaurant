from DB_Models.Menu.menu import *
from DB_Models.database import *
from DB_Models.Restaurant.restaurant import *
from sqlalchemy.orm import *
from sqlalchemy import *

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    # name = Column(String,nullable=False)
    quantity = Column(Integer,nullable=False)
    itemid = Column(Integer, ForeignKey("menu_item.id"),nullable=False)
    restaurantid = Column(Integer, ForeignKey("restaurant.id"),nullable=False)
    # restaurant = relationship("Restaurant",back_populates="prop_restaurant")
    # menu_item = relationship("Menu_Item",back_populates="prop_menu_item2")
