from sqlalchemy import Column, Integer, String
from models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    email = Column(String(255), unique=True)
