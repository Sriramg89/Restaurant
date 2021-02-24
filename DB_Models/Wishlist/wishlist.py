from ..Menu.menu import Menu_Category
from ..database import *



class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    categoryid = Column(Integer, ForeignKey('menu_category.id'))
    no_of_votes = Column(Integer)
    menu_category=relationship(Menu_Category)
