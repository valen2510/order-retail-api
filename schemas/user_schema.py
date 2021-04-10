"""
    Define schemas of data for user model
"""

from typing import Optional
from pydantic import BaseModel, EmailStr

class UserModelIn(BaseModel):
    name: str
    last_name: str
    gov_id: int
    email: Optional[str] = ""
    company: Optional[str] = ""

    class Config:
        orm_mode = True

class UserModelOut(UserModelIn):

    class Config:
        orm_mode = True