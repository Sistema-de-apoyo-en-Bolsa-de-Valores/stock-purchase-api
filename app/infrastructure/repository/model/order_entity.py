# app\infrastructure\repository\model\order_entity.py

from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, BigInteger
from app.infrastructure.repository.configuration.database_configuration import Base
from sqlalchemy.orm import relationship
from app.infrastructure.repository.model.user_entity import UserEntity

class OrderEntity(Base):
    __tablename__ = 'tb_orders'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('tb_users.id'), nullable=False)
    symbol = Column(String(10), nullable=False)
    sec_type = Column(String(10), nullable=False)
    exchange = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=True)
    status = Column(String(20), nullable=False)
    order_type = Column(String(10), nullable=False)
    order_id = Column(Integer, nullable=False)

    # Relación con el usuario
    users = relationship("UserEntity", back_populates="orders")