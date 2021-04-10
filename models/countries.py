"""
    Define class moddel for countries
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from ..models.base import Base


class Country(Base):
    """
       Country class to interact with the countries table from database
    """
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, nullable=False)
    country_name = Column(String(50), nullable=False)
    cost_shipping = Column(Integer, nullable=False)

    states = relationship('State', back_populates='state')