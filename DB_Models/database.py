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
