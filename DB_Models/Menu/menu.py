from ..database import *
from ..Restaurant.restaurant import *
from ..Menu.menu import *


class Menu_Category(Base):
    __tablename__ = "menu_category"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    restid = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)


class Menu_Item(Base):
    __tablename__ = "menu_item"

    id = Column(Integer, primary_key=True)
    categid = Column(Integer, ForeignKey("menu_category.id"))
    name = Column(String, unique=True)
    description = Column(String)
    cost = Column(Integer)
    gluten_free = Column(String)
    vegetarian = Column(String)
    menu_category = relationship(Menu_Category)
