"""Manejadores globales de excepciones."""
import logging

from fastapi import Request
from fastapi.responses import JSONResponse
from pymongo.errors import ServerSelectionTimeoutError

from app.core.exceptions import DomainException

logger = logging.getLogger(__name__)


def domain_exception_handler(request: Request, exception: DomainException) -> JSONResponse:
    """Maneja excepciones del dominio."""
    return JSONResponse(
        status_code=400,
        content={"detail": exception.message},
    )


def mongo_server_selection_timeout_handler(
    request: Request,
    exception: ServerSelectionTimeoutError,
) -> JSONResponse:
    """Maneja errores de conexion contra MongoDB."""
    logger.error("Base de datos no disponible: %s", exception)
    return JSONResponse(
        status_code=503,
        content={"detail": "Base de datos no disponible"},
    )
