#!/usr/bin/python3
"""Define City class"""
from model_state import Base, State
from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship


class City(Base):
    """City class with id and name attributes"""
    __tablename__ = 'cities'
    id = Column(autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", backref="state_id")
