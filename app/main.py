# app\main.py

from fastapi import FastAPI, HTTPException, Request
from app.infrastructure.rest.controllers.order_controller import router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.infrastructure.repository.configuration.database_configuration import create_tables
from datetime import date

app = FastAPI(
    title="stock-purchase-api",
    description=(
        "Esta API permite ejecutar órdenes de compra de acciones con la API de Interactive Brokers."
    ),
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    create_tables()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(content={"timestamp": date.today().isoformat(), "messages": [error['msg'] for error in exc.errors()]}, status_code=400)

app.include_router(router, prefix="/order", tags=["Endpoints sobre órdenes"])