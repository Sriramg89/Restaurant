from sqlalchemy.orm import backref, relationship
from DB_Models.database import *
from sqlalchemy import *


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    mobile = Column(Integer, unique=True,nullable=False)
    prop_user = relationship("Restaurant",backref="user")
    prop_user2 = relationship("Orders",backref="user")
    # orders= relationship("Orders",back_populates="user")
