from sqlalchemy import create_engine, column,String,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

DATABASE = "sqlite:///{DB}"

Base = declarative_base()

class user(Base):
    __tablename__ = "user"

    id = column('id',Integer,primary_key=True)
    first_name = column("first_name",String(25))
    last_name = column("last_name",String(25))
    username = column("username",Integer,unique=True)
    

