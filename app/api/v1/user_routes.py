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
def create_user(
    request: UserCreateRequest,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Crea un nuevo usuario."""
    try:
        return user_service.create_user(request)
    except ValidationException as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error.message,
        )


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Obtiene un usuario por ID."""
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )


@router.get("/", response_model=List[UserResponse])
def get_all_users(
    user_service: UserService = Depends(get_user_service),
) -> List[UserResponse]:
    """Obtiene todos los usuarios."""
    return user_service.get_all_users()


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    request: UserUpdateRequest,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Actualiza un usuario existente."""
    try:
        return user_service.update_user(user_id, request)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )


@router.patch("/{user_id}/deactivate", response_model=UserResponse)
def deactivate_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Desactiva un usuario."""
    try:
        return user_service.deactivate_user(user_id)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
) -> None:
    """Elimina un usuario."""
    try:
        user_service.delete_user(user_id)
    except NotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )
