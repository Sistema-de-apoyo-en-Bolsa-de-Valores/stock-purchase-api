# app\infrastructure\repository\configuration\database_configuration.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Crear la base declarativa
Base = declarative_base()

# Crear el motor de conexión
DATABASE_URL = (
    f"mysql+pymysql://root:root1234@mysql-arqui.cb4qaumg4edl.us-east-2.rds.amazonaws.com:3306/somesql"
)
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)