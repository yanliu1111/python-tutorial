# one to Many
import os
from sqlalchemy import (create_engine, Integer, String, Column, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
BASE_DIR =os.path.dirname(os.path.realpath(__file__))
conn = 'sqlite:///'+os.path.join(BASE_DIR,'blog.db')

engine = create_engine(conn,echo=True)
#specify echo=true meaning that we want to get all our generated SQL statements printed out to the console

Base  = declarative_base()

"""
class User:
    id: int pk
    username: str
    email: str

class Post:
    id: int pk
    title: str
    content: str
    user_id: int foreignkey
"""

class User(Base):
    __tablename__='users'
    id = Column (Integer(), primary_key=True)
    username = Column (String(40), nullable=False)
    email = Column (String(40), nullable=True)
    post = relationship('Post', back_populates='author', cascade="all, delete")
    # backref is finding out which user is the author of the post
    # cascade="all, delete" means that if we delete a user, all the posts related to that user will be deleted as well

    def __repr__(self):
        return f"<User {self.username}>"
    
class Post(Base):
    __tablename__='posts'
    id = Column (Integer(), primary_key=True)
    title = Column (String(45), nullable=False)
    content = Column (String(255), nullable=False)
    user_id = Column (Integer(), ForeignKey('users.id', ondelete='CASCADE'))
    # ondelete='CASCADE' means that if we delete a user, all the posts related to that user will be deleted as well
    author = relationship('User', back_populates='post', cascade="all, delete") # delete all posts or related post 

    def __repr__(self):
        return f"<Post {self.title}>"
    
Base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)