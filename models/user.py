"""
    Define class model for user
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from models.base import Base
from models import storage
import uuid

class User(Base):
    """
        User class to interact with the users table from database
    """
    __tablename__ = 'users'

    id = Column(String(80), primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gov_id = Column(Integer, unique=True, nullable=False)
    email = Column(String(80), unique=True)
    company = Column(String(80))


    def __init__(self, *args, **kwargs):
        """ Initialze user model """
        print(kwargs)
        if kwargs:
            for key, value in kwargs.items():
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
            storage.new(self)
            storage.save()
