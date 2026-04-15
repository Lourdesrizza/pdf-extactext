"""Manejadores globales de excepciones."""
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import DomainException


def domain_exception_handler(request: Request, exception: DomainException) -> JSONResponse:
    """Maneja excepciones del dominio."""
    return JSONResponse(
        status_code=400,
        content={"detail": exception.message},
    )
