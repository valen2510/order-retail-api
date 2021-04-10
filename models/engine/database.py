#!/usr/bin/python3
"""
    Define database class
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base import Base
from os import getenv


class Database:
    """ 
        Database class to interact with the postgres database
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize database object """
        PG_DB_URL = 'postgresql://test1:test123@localhost/tesdb'
        MYSQL_DB_URL= 'mysql://root:root@localhost/hbnb_dev_db'
        self.__engine = create_engine(PG_DB_URL)
    
    def connect(self):
        """ Initialize connection through session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
    
    def new(self, obj):
        """ Add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commint all changes to the current database session """
        self.__session.commit()

    def close(self):
        """ Close the currrent database session """
        self.__session.close()

    def get(self, cls, user_id):
        """Retrieve a certain object from the database"""
        try:
            value = self.__session.query(cls).filter(cls.id == user_id).first()
        except:
            value = None
        finally:
            return value
