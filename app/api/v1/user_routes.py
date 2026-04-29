"""Rutas API para gestión de usuarios."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.application.dto.user_dto import (
    UserCreateRequest,
    UserResponse,
    UserUpdateRequest,
)
from app.application.services.user_service import UserService
from app.core.exceptions import NotFoundException, ValidationException

from ..dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    request: UserCreateRequest,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Crea un nuevo usuario.

    Args:
        request: Datos del usuario a crear.

    Returns:
        Usuario creado con su ID asignado.

    Raises:
        HTTPException: 400 si el email ya está registrado.
    """
    try:
        return await user_service.create_user(request)
    except ValidationException as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error.message,
        )


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: str,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Obtiene un usuario por ID.

    Args:
        user_id: ID del usuario (string, formato MongoDB ObjectId).

    Returns:
        Usuario encontrado.

    Raises:
        HTTPException: 404 si el usuario no existe.
    """
    try:
        return await user_service.get_user_by_id(user_id)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )


@router.get("/", response_model=List[UserResponse])
async def get_all_users(
    user_service: UserService = Depends(get_user_service),
) -> List[UserResponse]:
    """Obtiene todos los usuarios.

    Returns:
        Lista de todos los usuarios registrados.
    """
    return await user_service.get_all_users()


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: str,
    request: UserUpdateRequest,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Actualiza un usuario existente.

    Args:
        user_id: ID del usuario a actualizar.
        request: Datos actualizados del usuario.

    Returns:
        Usuario actualizado.

    Raises:
        HTTPException: 404 si el usuario no existe.
    """
    try:
        return await user_service.update_user(user_id, request)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )


@router.patch("/{user_id}/deactivate", response_model=UserResponse)
async def deactivate_user(
    user_id: str,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Desactiva un usuario.

    Args:
        user_id: ID del usuario a desactivar.

    Returns:
        Usuario desactivado.

    Raises:
        HTTPException: 404 si el usuario no existe.
    """
    try:
        return await user_service.deactivate_user(user_id)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: str,
    user_service: UserService = Depends(get_user_service),
) -> None:
    """Elimina un usuario.

    Args:
        user_id: ID del usuario a eliminar.

    Raises:
        HTTPException: 404 si el usuario no existe.
    """
    try:
        await user_service.delete_user(user_id)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )
