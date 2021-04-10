"""
    Define class moddel for cities
"""

from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship
from ..models.base import Base


class City(Base):
    """
       State class to interact with the cities table from database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    city_name = Column(String(50), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    city = relationship('State', back_populates='cities')
