"""Implementación SQL del repositorio de usuarios."""
from typing import List, Optional

from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.models.user_model import UserModel


class SqlUserRepository(UserRepository):
    """Repositorio de usuarios usando SQLAlchemy."""

    def __init__(self, database_session: Session) -> None:
        self._session = database_session

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Busca un usuario por su ID."""
        model = self._session.query(UserModel).filter(UserModel.id == user_id).first()
        return self._to_entity(model) if model else None

    def find_by_email(self, email: str) -> Optional[User]:
        """Busca un usuario por su email."""
        model = self._session.query(UserModel).filter(UserModel.email == email).first()
        return self._to_entity(model) if model else None

    def find_all(self) -> List[User]:
        """Obtiene todos los usuarios."""
        models = self._session.query(UserModel).all()
        return [self._to_entity(model) for model in models]

    def create(self, user: User) -> User:
        """Crea un nuevo usuario."""
        model = UserModel(
            email=user.email,
            full_name=user.full_name,
            is_active=user.is_active,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)

    def update(self, user: User) -> User:
        """Actualiza un usuario existente."""
        model = self._session.query(UserModel).filter(UserModel.id == user.id).first()
        if model:
            model.full_name = user.full_name
            model.is_active = user.is_active
            self._session.commit()
            self._session.refresh(model)
        return self._to_entity(model) if model else user

    def delete(self, user_id: int) -> None:
        """Elimina un usuario por su ID."""
        model = self._session.query(UserModel).filter(UserModel.id == user_id).first()
        if model:
            self._session.delete(model)
            self._session.commit()

    def _to_entity(self, model: UserModel) -> User:
        """Convierte modelo a entidad de dominio."""
        return User(
            id=model.id,
            email=model.email,
            full_name=model.full_name,
            is_active=model.is_active,
            created_at=model.created_at,
        )
