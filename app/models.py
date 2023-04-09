from app.db import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    posts = relationship("Post", backref="author")


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    content = Column(String(255), nullable=False)
