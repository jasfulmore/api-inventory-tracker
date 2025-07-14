from pydantic import BaseModel
from typing import Optional


class ItemCreate(BaseModel):
    id: int
    name: str
    quantity: int
    price: float



class ItemUpdate(BaseModel):
    quantity: Optional[int]
    price: Optional[float]

