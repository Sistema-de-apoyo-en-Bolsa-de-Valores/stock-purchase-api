# app\infrastructure\rest\model\buy_stock_request.py

from pydantic import BaseModel, constr, conint, Field
from typing import Optional

class BuyStockRequest(BaseModel):
    symbol: constr(strip_whitespace=True, min_length=1, max_length=10)
    sec_type: constr(strip_whitespace=True, min_length=1, max_length=10)
    exchange: constr(strip_whitespace=True, min_length=1, max_length=10)
    quantity: conint(gt=0)
    order_type: constr(strip_whitespace=True, min_length=1, max_length=10)
    price: Optional[float] = Field(None, gt=0, description="El precio debe ser positivo si se especifica.")