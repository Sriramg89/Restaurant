from ..database import *


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    age = Column(Integer)
    mobile = Column(Integer, unique=True)
