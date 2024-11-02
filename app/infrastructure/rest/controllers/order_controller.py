# app\infrastructure\rest\controllers\order_controller.py

from fastapi import APIRouter, HTTPException, Depends, Query
from app.application.service.order_service import OrderService
from app.infrastructure.rest.model.buy_stock_request import BuyStockRequest
from fastapi.responses import JSONResponse
from app.infrastructure.configuration.dependencies import get_order_service
from datetime import date

router = APIRouter()

@router.post(
    "/buy", 
    summary="Endpoint para ejecutar órdenes de compra de acciones.", 
    description="Se ejecuta la orden de compra de acciones y se almacena la información en base de datos.")
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
        return JSONResponse(content=order.dict(), status_code=201)
    except Exception as e:
        return JSONResponse(content={"timestamp": date.today().isoformat(), "messages": [str(e)]}, status_code=500)

@router.get("", summary="Endpoint para obtener órdenes por ID de un usuario.", 
description="Se filtran las órdenes ejecutadas por un usuario en específico."
)
def get_orders_by_user(
    user: int = Query(..., gt=0, description="ID del usuario del cual se extraen sus órdenes."),
    order_service: OrderService = Depends(get_order_service)
):
    try:
        orders = order_service.get_orders_by_user(user_id=user)
        return JSONResponse(content=[order.dict() for order in orders], status_code=200)
    except Exception as e:
        return JSONResponse(content={"timestamp": date.today().isoformat(), "messages": [str(e)]}, status_code=500)