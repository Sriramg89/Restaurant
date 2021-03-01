from DB_Models.database import *
from DB_Models.Restaurant.restaurant import *
from DB_Models.Menu.menu import *
from sqlalchemy import *
from sqlalchemy.orm import *

class Menu_Category(Base):
    __tablename__ = "menu_category"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    restid = Column(Integer, ForeignKey("restaurant.id"), nullable=False)
    # restaurant = relationship("Restaurant",back_populates="prop_menu_category") 
    # menu_item= relationship("Menu_Item",back_populates="menu_category")
    # wishlist = relationship("Wishlist",back_populates="menu_category")
    prop_menu_category = relationship("Menu_Item",backref="menu_category")
    # prop_menu_category2 = relationship("Menu_Item",back_populates="menu_category")
    prop_menu_category2 = relationship("Wishlist", backref="menu_category")
class Menu_Item(Base):
    __tablename__ = "menu_item"

    id = Column(Integer, primary_key=True)
    categid = Column(Integer, ForeignKey("menu_category.id"), nullable=False)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    cost = Column(Integer,nullable=False)
    gluten_free = Column(String)
    vegetarian = Column(String)
    # menu_category = relationship("Menu_Category",back_populates="prop_menu_category2")
    inventory_prop = relationship("Inventory",backref="menu_item")
    # orders= relationship("Orders",back_populates="menu_category")
    # menu_item_prop= relationship("Orders",back_populates="menu_item")
    # prop_menu_item2= relationship("Inventory",back_populates="menu_item")
    prop_user2 = relationship("Orders",backref="menu_item")