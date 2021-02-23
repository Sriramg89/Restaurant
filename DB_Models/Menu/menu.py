from ..database import *
from ..Restaurant.restaurant import *


class Menu_Category(Base):
    __tablename__ = "menu_cat"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    restid = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)


class Menu_Item(Base):
    __tablename__ = "menu_item"

    id = Column(Integer, primary_key=True)
    categid = Column(Integer, ForeignKey("menu_cat.id"))
    name = Column(String, unique=True)
    description = Column(String)
    cost = Column(Integer)
    gluten_free = Column(String)
    vegetarian = Column(String)
    menu_cat = relationship(Menu_Category)
