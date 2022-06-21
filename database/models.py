from operator import index
from .db import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    active = Column(Boolean, default=True)
    age = Column(Integer)

    posts = relationship('Post', back_populates='author')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    
    author = relationship('User', back_populates='posts')
