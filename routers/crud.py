from ..models import storage
from ..models.user import User
from ..models.order import Order


def get_user(user_id: str):
    response = 
    return response

def get_users():
    return storage._Database__session.query(User).all()

def get_orders():
    return storage.query(Order).all()