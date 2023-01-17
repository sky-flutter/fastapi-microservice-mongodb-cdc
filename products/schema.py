from pydantic import BaseModel
from typing import Optional
class ProductCreate(BaseModel):
    name: str
    description: str
    discount_price: float
    final_price: float
    slug: str

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    discount_price: Optional[float]
    final_price: Optional[float]
    slug: Optional[str]
    id: str