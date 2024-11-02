# app\infrastructure\repository\model\user_entity.py

from sqlalchemy import Column, String, BigInteger
from app.infrastructure.repository.configuration.database_configuration import Base
from sqlalchemy.orm import relationship

class UserEntity(Base):
    __tablename__ = 'tb_users'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    # Otros campos de la tabla tb_users, por ejemplo:
    email = Column(String(320), nullable=False, unique=True)
    lastname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    password = Column(String(60), nullable=False)

    # Relación inversa con las órdenes
    orders = relationship("OrderEntity", back_populates="users", cascade="all, delete-orphan")