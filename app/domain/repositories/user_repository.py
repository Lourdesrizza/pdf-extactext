"""Interfaz del repositorio de usuarios."""

from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import User


class UserRepository(ABC):
    """Contrato para operaciones de persistencia de usuarios.

    Esta interfaz es agnóstica a la implementación de base de datos.
    Todos los métodos son async para soportar operaciones no bloqueantes.
    Los IDs son strings para soportar MongoDB ObjectId.
    """

    @abstractmethod
    async def find_by_id(self, user_id: str) -> Optional[User]:
        """Busca un usuario por su ID.

        Args:
            user_id: ID del usuario como string.

        Returns:
            Entidad User si existe, None si no se encuentra.
        """
        raise NotImplementedError

    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[User]:
        """Busca un usuario por su email.

        Args:
            email: Email del usuario.

        Returns:
            Entidad User si existe, None si no se encuentra.
        """
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> List[User]:
        """Obtiene todos los usuarios.

        Returns:
            Lista de entidades User.
        """
        raise NotImplementedError

    @abstractmethod
    async def create(self, user: User) -> User:
        """Crea un nuevo usuario.

        Args:
            user: Entidad User a crear.

        Returns:
            Entidad User creada con ID asignado.
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, user: User) -> User:
        """Actualiza un usuario existente.

        Args:
            user: Entidad User con datos actualizados.

        Returns:
            Entidad User actualizada.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, user_id: str) -> None:
        """Elimina un usuario por su ID.

        Args:
            user_id: ID del usuario a eliminar.
        """
        raise NotImplementedError
