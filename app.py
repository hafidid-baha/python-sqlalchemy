from sqlalchemy import create_engine, column,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

DATABASE = "sqlite:///{DB}"

Base = declarative_base()



