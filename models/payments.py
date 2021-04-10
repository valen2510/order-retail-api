"""
    Define class model for payments
"""

from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from ..models.base import Base
from datetime import datetime
import enum

class Payment_Type(enum.Enum):
    """
        Enumerated type for payment method
    """
    credit_car = 'Credit Card'
    debit_card = 'Debit Card'
    cash = 'Cash'

class Payment(Base):
    """
       Payment class to interact with the Payments table from database
    """
    __tablename__ = 'Payments'

    id = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'))
    payment_type = Column(Enum(Payment_Type))
    payment_date = Column(DateTime)
    total = Column(Integer, nullable=False)
    status = Column(Boolean)

    order = relationship('Order', back_populates='Payments')

    __nb_intances = 0

    def __init__(self, *args, **kwargs):
        """ Initialze Payment model """
        if kwargs:
            for key, value in kwargs.items():
                    setattr(self, key, value)
            Payment.__nb_intances += 1
            self.id =Payment.__nb_intances
            self.payment_date = datetime.now()
            storage.new(self)
            storage.save()