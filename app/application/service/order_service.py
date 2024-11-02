# app\application\service\order_service.py

from app.infrastructure.interactive_broker.ibkr_client import IBapiClient
from app.infrastructure.repository.adapter.order_repository_adapter import OrderRepositoryAdapter
from app.domain.model.order import Order
from typing import List

class OrderService:
    def __init__(self, ib_client: IBapiClient, order_repository_adapter: OrderRepositoryAdapter):
        self.ib_client = ib_client
        self.order_repository_adapter = order_repository_adapter

    def place_order(self, user_id: int, symbol: str, sec_type: str, exchange: str, quantity: int, order_type: str, price: float):
        order_id = self.ib_client.place_order(symbol, sec_type, exchange, quantity, order_type, price)
        
        order = Order(
            user_id=user_id,
            symbol=symbol,
            sec_type=sec_type,
            exchange=exchange,
            quantity=quantity,
            price=price,
            status="executed",
            order_type=order_type,
            order_id=order_id
        )
            
        # Utilizar el repositorio para guardar la orden
        self.order_repository_adapter.save(order)
        return order

    def get_orders_by_user(self, user_id: int) -> List[Order]:
        # Utiliza el repositorio para obtener todas las órdenes del usuario especificado
        return self.order_repository_adapter.get_orders_by_user(user_id)