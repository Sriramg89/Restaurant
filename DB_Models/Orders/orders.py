from sqlalchemy.orm import *
from sqlalchemy import *
from DB_Models.Menu.menu import *
from DB_Models.database import *
from DB_Models.User.user import *
from DB_Models.Restaurant.restaurant import *


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey("user.id"), nullable=False)
    restid = Column(Integer, ForeignKey("restaurant.id"), nullable=False)
    description = Column(String)
    date = Column(DateTime, nullable=False)
    itemid = Column(Integer, ForeignKey("menu_item.id"), nullable=False)
    # menu_item = relationship("Menu_Item",back_populates="menu_item_prop")
    quantity = Column(Integer, nullable=False)
    # user = relationship("User",back_populates="prop_user2")
    # restaurant = relationship("Restaurant",back_populates="prop_restaurant2")
