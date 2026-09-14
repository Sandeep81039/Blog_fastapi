from sqlalchemy import Column,Integer,String,Text
from database import Base

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    contant = Column(Text)
     

class UserRegister(Base):
    __tablename__ = "userdata"
    username = Column(String,primary_key=True)
    password = Column(String)
    