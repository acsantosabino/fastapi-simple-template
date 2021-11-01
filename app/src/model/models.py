"""
models define modelos de dados da api
"""
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    """ Item exemplo """
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
