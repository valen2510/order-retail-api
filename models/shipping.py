"""
    Define class moddel for shipping
"""

from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..models.base import Base

class Shipping(Base):
    """
        Shipping class to interact with the shipping table from database
    """
    __tablename__ = 'shipping'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(String(80), ForeignKey('users.id'))
    address = Column(String(100), nullable=False)
    city = Column(String(30), ForeignKey('cities.id'))
    state = Column(String(30), ForeignKey('states.id'))
    country_id = Column(Integer, ForeignKey('countries.id'))
    cost  = Column(Integer, nullable=False)

    #user = relationship('User', back_populates='shipping')
    country = relationship('Country', back_populates='shipping')

    __nb_intances = 0

    def __init__(self, *args, **kwargs):
        """ Initialze shipping model """
        if kwargs:
            for key, value in kwargs.items():
                    setattr(self, key, value)
            Shipping.__nb_intances += 1
            self.id = Shipping.__nb_intances
            storage.new(self)
            storage.save()