import os
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = f"sqlite:///"+os.path.join(BASE_DIR, 'site.db')

Base = declarative_base()

engine = create_engine(connection_string, echo=True) # echo=True: show the sql query are generated on carring out any sql query or any database task for example, if we create db, it shows us the various commands that are going to be run onto db creator tables and if we add or change or delete or update anything, it is going to show us the sql is done for that particular task

"""
class User
    id int
    username str
    email str
    date_created datetime
"""

class User(Base):
    __tablename__='users' 
    id = Column(Integer(), primary_key=True)
    username = Column(Integer(), primary_key=True)
    username= Column(String(25),nullable=False,unique=True)
    email = Column(String(80),nullable=False,unique=True)
    data_created= Column(DateTime(),default=datetime.utcnow) # utconw: sepcify the date at that particular time
    #return a string representation of the object
    def __repr__(self):
        return f"<User username={self.username}, email={self.email}>"
new_user = User(id=1, username='Bob', email='bob@test.com')
print(new_user)
# <__main__.User object at 0x000001D7CB6940D0> location of the object in memory