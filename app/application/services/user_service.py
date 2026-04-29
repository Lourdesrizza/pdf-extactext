"""Servicio de aplicación para gestión de usuarios."""

from typing import List

from app.core.exceptions import NotFoundException, ValidationException
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository

from ..dto.user_dto import UserCreateRequest, UserResponse, UserUpdateRequest


class UserService:
    """Caso de uso: Gestión de usuarios.

    Servicio de aplicación que coordina operaciones CRUD de usuarios.
    Trabaja con IDs string para soportar MongoDB ObjectId.
    Todos los métodos son async para operaciones no bloqueantes.
    """

    def __init__(self, user_repository: UserRepository) -> None:
        """Inicializa el servicio con un repositorio de usuarios.

        Args:
            user_repository: Implementación de UserRepository.
        """
        self._repository = user_repository

    async def create_user(self, request: UserCreateRequest) -> UserResponse:
        """Crea un nuevo usuario.

        Args:
            request: DTO con datos del nuevo usuario.

        Returns:
            DTO de respuesta con el usuario creado.

        Raises:
            ValidationException: Si el email ya está registrado.
        """
        existing_user = await self._repository.find_by_email(request.email)
        if existing_user:
            raise ValidationException("email", "El email ya está registrado")

        user = User(email=request.email, full_name=request.full_name)
        created_user = await self._repository.create(user)

        return self._map_to_response(created_user)

    async def get_user_by_id(self, user_id: str) -> UserResponse:
        """Obtiene un usuario por ID.

        Args:
            user_id: ID del usuario (string).

        Returns:
            DTO de respuesta con el usuario.

        Raises:
            NotFoundException: Si el usuario no existe.
        """
        user = await self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", user_id)

        return self._map_to_response(user)

    async def get_all_users(self) -> List[UserResponse]:
        """Obtiene todos los usuarios.

        Returns:
            Lista de DTOs de respuesta con todos los usuarios.
        """
        users = await self._repository.find_all()
        return [self._map_to_response(user) for user in users]

    async def update_user(
        self, user_id: str, request: UserUpdateRequest
    ) -> UserResponse:
        """Actualiza un usuario existente.

        Args:
            user_id: ID del usuario a actualizar.
            request: DTO con datos actualizados.

        Returns:
            DTO de respuesta con el usuario actualizado.

        Raises:
            NotFoundException: Si el usuario no existe.
        """
        user = await self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", user_id)

        user.update_profile(request.full_name)
        updated_user = await self._repository.update(user)

        return self._map_to_response(updated_user)

    async def deactivate_user(self, user_id: str) -> UserResponse:
        """Desactiva un usuario.

        Args:
            user_id: ID del usuario a desactivar.

        Returns:
            DTO de respuesta con el usuario desactivado.

        Raises:
            NotFoundException: Si el usuario no existe.
        """
        user = await self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", user_id)

        user.deactivate()
        updated_user = await self._repository.update(user)

        return self._map_to_response(updated_user)

    async def delete_user(self, user_id: str) -> None:
        """Elimina un usuario.

        Args:
            user_id: ID del usuario a eliminar.

        Raises:
            NotFoundException: Si el usuario no existe.
        """
        user = await self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", user_id)

        await self._repository.delete(user_id)

    def _map_to_response(self, user: User) -> UserResponse:
        """Mapea una entidad a DTO de respuesta.

        Args:
            user: Entidad de dominio User.

        Returns:
            DTO de respuesta UserResponse.
        """
        return UserResponse(
            id=user.id or "",
            email=user.email,
            full_name=user.full_name,
            is_active=user.is_active,
            created_at=user.created_at,
        )
