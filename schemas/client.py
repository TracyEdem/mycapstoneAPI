from pydantic import BaseModel
from enum import Enum
from models.client import Gender


class Client(BaseModel):
    # clientId: int
    name: str
    phone_no: str
    gender: Gender = 'Female'
    balance: float
    # userId: int