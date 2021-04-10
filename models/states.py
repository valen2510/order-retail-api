"""
    Define class moddel for states
"""

from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship
from ..models.base import Base


class State(Base):
    """
       State class to interact with the states table from database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    state_name = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'))

    state = relationship('Country', back_populates='states')
    cities = relationship('City', back_populates='city')
