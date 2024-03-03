from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Friend(Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True)
    peer_1 = Column(String, nullable=False)
    peer_2 = Column(String, nullable=False)


class Invite(Base):
    __tablename__ = 'invite'

    id = Column(Integer, primary_key=True)
    peer_1 = Column(String, nullable=False)
    peer_2 = Column(String, nullable=False)
    is_closed = Column(Boolean, default=False)
