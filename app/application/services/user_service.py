"""Servicio de aplicación para gestión de usuarios."""
from typing import List

from app.core.exceptions import NotFoundException, ValidationException
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository

from ..dto.user_dto import UserCreateRequest, UserResponse, UserUpdateRequest


class UserService:
    """Caso de uso: Gestión de usuarios."""

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository = user_repository

    def create_user(self, request: UserCreateRequest) -> UserResponse:
        """Crea un nuevo usuario."""
        existing_user = self._repository.find_by_email(request.email)
        if existing_user:
            raise ValidationException("email", "El email ya está registrado")

        user = User(email=request.email, full_name=request.full_name)
        created_user = self._repository.create(user)

        return self._map_to_response(created_user)

    def get_user_by_id(self, user_id: int) -> UserResponse:
        """Obtiene un usuario por ID."""
        user = self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", str(user_id))

        return self._map_to_response(user)

    def get_all_users(self) -> List[UserResponse]:
        """Obtiene todos los usuarios."""
        users = self._repository.find_all()
        return [self._map_to_response(user) for user in users]

    def update_user(self, user_id: int, request: UserUpdateRequest) -> UserResponse:
        """Actualiza un usuario existente."""
        user = self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", str(user_id))

        user.update_profile(request.full_name)
        updated_user = self._repository.update(user)

        return self._map_to_response(updated_user)

    def deactivate_user(self, user_id: int) -> UserResponse:
        """Desactiva un usuario."""
        user = self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", str(user_id))

        user.deactivate()
        updated_user = self._repository.update(user)

        return self._map_to_response(updated_user)

    def delete_user(self, user_id: int) -> None:
        """Elimina un usuario."""
        user = self._repository.find_by_id(user_id)
        if not user:
            raise NotFoundException("Usuario", str(user_id))

        self._repository.delete(user_id)

    def _map_to_response(self, user: User) -> UserResponse:
        """Mapea una entidad a DTO de respuesta."""
        return UserResponse(
            id=user.id or 0,
            email=user.email,
            full_name=user.full_name,
            is_active=user.is_active,
        )
