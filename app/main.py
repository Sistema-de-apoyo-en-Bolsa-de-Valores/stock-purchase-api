# app\main.py

from fastapi import FastAPI, HTTPException, Request
from app.infrastructure.rest.controllers.order_controller import router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.infrastructure.repository.configuration.database_configuration import create_tables
from pydantic import ValidationError

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_tables()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(content={"status": "error", "detail": exc.errors()}, status_code=400)

app.include_router(router, prefix="/order", tags=["order"])