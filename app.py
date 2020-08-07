from sqlalchemy import create_engine,String,Integer,ForeignKey,MetaData,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

DATABASE = "sqlite:///{}"

metadata = MetaData()
Base = declarative_base()

class user(Base):
    __tablename__ = "user"

    id = Column('id',Integer, primary_key=True)
    first_name = Column("first_name",String(25))
    last_name = Column("last_name",String(25))
    username = Column("username",Integer,unique=True)


## create the engine 
engine = create_engine(DATABASE.format("data.db"))
## create all tables using the base classe
Base.metadata.create_all(bind=engine)

## use the session maker to create a session and bind it with the engin
session = sessionmaker(bind=engine)
## create actual session object
session = session()
user = user()
user.id = 1
user.first_name = "hafid"
user.last_name = "id-baha"
user.username = "foxin"

##add the created object to the session
session.add(user)
session.commit()

session.close()

    

