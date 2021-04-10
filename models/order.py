"""
    Define class moddel for order
"""

from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime

class Order(Base):
    """
        Order class to interact with the orders table from database
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(String(80), ForeignKey('users.id'))
    shipping_id = Column(String(80), ForeignKey('shipping.id'))
    order_date = Column(DateTime)
    subtotal = Column(Integer, nullable=False)
    taxes = Column(Integer, nullable=False)
    total = Column(Integer)
    paid = Column(Boolean, default=False)

    user = relationship('User')

    __nb_intances = 0

    def __init__(self, *args, **kwargs):
        """ Initialze order model """
        if kwargs:
            for key, value in kwargs.items():
                    setattr(self, key, value)
            Order.__nb_intances += 1
            self.id = Order.__nb_intances
            self.order_date = datetime.now()
            storage.new(self)
            storage.save()
