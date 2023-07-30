from sqlalchemy import Column, Integer, String
from models.base import Base


class Guild(Base):
    __tablename__ = 'guilds'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    owner_id = Column(Integer)
