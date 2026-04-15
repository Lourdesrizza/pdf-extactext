"""Interfaz del repositorio de usuarios."""
from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import User


class UserRepository(ABC):
    """Contrato para operaciones de persistencia de usuarios."""

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        """Busca un usuario por su ID."""
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """Busca un usuario por su email."""
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[User]:
        """Obtiene todos los usuarios."""
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> User:
        """Crea un nuevo usuario."""
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> User:
        """Actualiza un usuario existente."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: int) -> None:
        """Elimina un usuario por su ID."""
        raise NotImplementedError
