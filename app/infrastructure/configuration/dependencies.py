# app\infrastructure\configuration\dependencies.py

from fastapi import Depends
from app.infrastructure.interactive_broker.ibkr_client import IBapiClient
from app.infrastructure.repository.adapter.order_repository_adapter import OrderRepositoryAdapter
from app.application.service.order_service import OrderService

def get_ib_client():
    return IBapiClient()

def get_order_repository_adapter():
    return OrderRepositoryAdapter()

def get_order_service(
    ib_client: IBapiClient = Depends(get_ib_client),
    order_repository_adapter: OrderRepositoryAdapter = Depends(get_order_repository_adapter)
):
    return OrderService(ib_client, order_repository_adapter)