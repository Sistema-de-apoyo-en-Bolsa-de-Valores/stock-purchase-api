# app\infrastructure\rest\controllers\order_controller.py

from fastapi import APIRouter, HTTPException
from app.application.service.order_service import OrderService
from app.infrastructure.rest.model.buy_stock_request import BuyStockRequest
from pydantic import constr
from fastapi.responses import JSONResponse
from app.infrastructure.configuration.dependencies import get_order_service
from fastapi import Depends

router = APIRouter()

@router.post("/buy")
def buy_stock(request: BuyStockRequest, order_service: OrderService = Depends(get_order_service)):
    try:
        order = order_service.place_order(
            user_id=request.user_id,
            symbol=request.symbol,
            sec_type=request.sec_type,
            exchange=request.exchange,
            quantity=request.quantity,
            order_type=request.order_type,
            price=request.price
        )
        return JSONResponse(content={"status": "success", "order": order.dict()}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"status": "error", "detail": str(e)}, status_code=500)