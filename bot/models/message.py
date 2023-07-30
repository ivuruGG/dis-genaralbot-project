from sqlalchemy import Column, Integer, String
from models.base import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    content = Column(String(255))
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates="messages")
