"""Dependencias de inyección para FastAPI."""
from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.user_service import UserService
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.connection import get_database_session
from app.infrastructure.repositories.sql_user_repository import SqlUserRepository


def get_user_repository(
    database_session: Session = Depends(get_database_session),
) -> UserRepository:
    """Provee el repositorio de usuarios."""
    return SqlUserRepository(database_session)


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    """Provee el servicio de usuarios."""
    return UserService(user_repository)
