"""
    Define path operation of orders
"""

from fastapi import APIRouter
from typing import List
from models import storage
from schemas import schemas
from models.order import Order

router = APIRouter(
    prefix='/orders',
    responses={404: {"description": "Not found"}}
)

@router.post('/')
def create_order(order: schemas.Order):
    """
        Create a new order
    """
    instance = Order(**order.__dict__)
    return instance

@router.get('/{order_id}', response_model=schemas.Order)
def get_order(order_id: int):
    """
        Retrieve an order
    """
    order = storage._Database__session.query(Order).filter(Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get('/{orders_ids}', response_model=List[schemas.Order])
def get_orders(orders_ids):
    """ 
        Retrieves the info of all order objects
    """
    return storage._Database__session.query(Order).all()

@router.get('/{dates}')
def get_orders_by_dates(dates):
     """ 
        Retrieves the ids of the order objects between the dates
    """

@router.get('/{user_id}')
def get_orders_by_user(user_id: str):
     """ 
        Retrieves the orders from the given user id
    """

@router.get('/shipping/{key_string}')
def get_orders_by_location(key_string):
     """ 
        Retrieves the orders from the given location
    """

@router.get('/{search_term}')
def get_orders_by_location(search_term):
     """ 
        Retrieves the orders from the given search term
    """

    