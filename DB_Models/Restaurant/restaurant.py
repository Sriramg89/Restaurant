from sqlalchemy import *
from DB_Models.database import *
from DB_Models.User.user import *
from sqlalchemy.orm import *


class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String, unique=True)
    open_time = Column(Time, nullable=False)
    close_time = Column(Time, nullable=False)
    rating = Column(Integer, nullable=False)
    average_cost = Column(Integer, nullable=False)
    userid = Column(Integer, ForeignKey("user.id"), nullable=False)
    prop_order = relationship("Orders",backref="restaurant")
    prop_restaurant = relationship("Menu_Category",backref="restaurant") 

    # user = relationship("User",back_populates="prop_user")
    prop_restaurant2 = relationship("Inventory",backref="restaurant")
    # prop_menu_category= relationship("Menu_Category",back_populates="restaurant")
    # orders= relationship("Orders",back_populates="restaurant")
    # prop_restaurant2 = relationship("Orders",back_populates="restaurant")