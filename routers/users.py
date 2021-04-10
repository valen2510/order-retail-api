"""
    Define path operation of users
"""

from fastapi import APIRouter, HTTPException
from typing import List
from models import storage
from schemas.user_schema import UserModelIn, UserModelOut
from models.user import User

router = APIRouter(
    prefix='/users',
    responses={404: {"description": "Not found"}}
)

@router.post('/')
def create_user(user: UserModelIn):
    """
        Create a new user
    """
    return User(**user.__dict__)

@router.get('/all')
def get_all_users():
    """ 
        Retrieves the list of all user objects
    """
    print(User)
    return storage._Database__session.query(User).all()

@router.get('/{user_id}', response_model=UserModelIn)
def get_user(user_id: str):
    """ 
        Retrieves an user
    """
    user = storage.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user