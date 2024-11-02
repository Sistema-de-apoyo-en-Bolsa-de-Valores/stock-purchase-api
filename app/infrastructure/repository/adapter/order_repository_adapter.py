# app\infrastructure\repository\adapter\order_repository_adapter.py

from app.infrastructure.repository.configuration.database_configuration import SessionLocal
from app.domain.model.order import Order
from app.infrastructure.repository.model.order_entity import OrderEntity
from sqlalchemy.exc import SQLAlchemyError

class OrderRepositoryAdapter:
    def __init__(self):
        self.session = SessionLocal()

    def save(self, order: Order):
        try:
            order_model = OrderEntity(
                user_id=order.user_id,
                symbol=order.symbol,
                sec_type=order.sec_type,
                exchange=order.exchange,
                quantity=order.quantity,
                price=order.price,
                status=order.status,
                order_type=order.order_type,
                order_id=order.order_id
            )
            self.session.add(order_model)
            self.session.commit()
            return order_model
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()