from pydantic import BaseModel
class OrderCreate(BaseModel):
    product_id: str
    discount_price: float
    tax: float
    final_price: float
    slug: str