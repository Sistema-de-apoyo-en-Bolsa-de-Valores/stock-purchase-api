# app\domain\model\order.py
from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    user_id: int
    symbol: str
    sec_type: str
    exchange: str
    quantity: int
    price: float
    status: str
    order_type: str
    order_id: Optional[int] = None