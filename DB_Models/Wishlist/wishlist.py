from DB_Models.Menu.menu import Menu_Category
from DB_Models.database import *
from sqlalchemy import *
from sqlalchemy.orm import *

class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    categoryid = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    no_of_votes = Column(Integer)
    # menu_category = relationship("Menu_Category", backref="prop_menu_category")
