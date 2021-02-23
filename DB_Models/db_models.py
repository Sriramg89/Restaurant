import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy import Boolean, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.schema import ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import DateTime

SQLALCHEMY_DATABASE_URL = "sqlite:///./restaurant.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class Restaurant(Base):
    __tablename__ = "restrnt"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    open_time = Column(String)
    close_time = Column(String)
    userid = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)


class Menu_Category(Base):
    __tablename__ = "menu_cat"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    restid = Column(Integer, ForeignKey("restrnt.id"))
    restrnt = relationship(Restaurant)


class Menu_Item(Base):
    __tablename__ = "menu_item"

    id = Column(Integer, primary_key=True)
    categid = Column(Integer, ForeignKey("menu_cat.id"))
    name = Column(String)
    description = Column(String)
    cost = Column(Integer)
    menu_cat = relationship(Menu_Category)
