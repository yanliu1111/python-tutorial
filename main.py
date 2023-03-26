from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
Base = declarative_base()

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