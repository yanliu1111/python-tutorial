import os

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker # sessionmaker is a function that creates a session object

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conn_str='sqlite:///' + os.path.join(BASE_DIR, 'data.db')

engine = create_engine(conn_str, echo= True) # create_engine is a function that creates a connection to the database

Base = declarative_base()

'''
class Parent:
    id: int pk
    name: str

class Child:
    id: int pk
    name: str
    parent_id: int fk (Parent.id)
'''

class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)
    children = relationship('Child', back_populates='parent', uselist = False, cascade="all, delete") # uselist = False means that there is only one instance of Child to related to the specific Parent
    def __repr__(self):
        return f"<Parent {self.id}>"
    
class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False)
    parent_id = Column(Integer(), ForeignKey('parents.id', ondelete='CASCADE'))
    parent = relationship('Parent', back_populates='children') # back_populates is the opposite of children in Parent

    def __repr__(self):
        return f"<Child {self.id}>"
    
    
      # create the tables
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)() # session is an instance of the sessionmaker function