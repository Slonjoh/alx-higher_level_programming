#!/usr/bin/python3
"""Define City class"""
from relationship_state import Base, State
from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship


class City(Base):
    """City class with id and name attributes"""
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
