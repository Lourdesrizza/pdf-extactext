"""Punto de entrada de la aplicación FastAPI."""
from fastapi import FastAPI

from app.api.exception_handlers import domain_exception_handler
from app.api.routes import user_routes
from app.core.config import settings
from app.core.exceptions import DomainException


def create_application() -> FastAPI:
    """Factory para crear la aplicación FastAPI."""
    application = FastAPI(
        title=settings.app_name,
        debug=settings.debug_mode,
    )

    # Registro de manejadores de excepciones
    application.add_exception_handler(DomainException, domain_exception_handler)

    # Registro de rutas
    application.include_router(user_routes.router)

    return application


app = create_application()
