from pydantic import BaseModel
from typing import Optional

#models
class ItemCreate(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
    reorder_lvl = int



class ItemUpdate(BaseModel):
    quantity: Optional[int]
    price: Optional[float]
    reorder_lvl = Optional[int]


