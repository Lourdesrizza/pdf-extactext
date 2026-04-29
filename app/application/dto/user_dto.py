"""DTOs para transferencia de datos de usuarios."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreateRequest(BaseModel):
    """DTO para crear un usuario."""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "usuario@ejemplo.com",
                "full_name": "Nombre Completo",
            }
        }
    )

    email: EmailStr = Field(..., description="Correo electrónico del usuario")
    full_name: str = Field(
        ..., min_length=1, max_length=255, description="Nombre completo del usuario"
    )


class UserUpdateRequest(BaseModel):
    """DTO para actualizar un usuario."""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "full_name": "Nuevo Nombre",
            }
        }
    )

    full_name: str = Field(
        ..., min_length=1, max_length=255, description="Nombre completo del usuario"
    )


class UserResponse(BaseModel):
    """DTO para respuesta de usuario."""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "email": "usuario@ejemplo.com",
                "full_name": "Nombre Completo",
                "is_active": True,
                "created_at": "2024-01-01T00:00:00",
            }
        }
    )

    id: str = Field(..., description="ID único de MongoDB (string)")
    email: str = Field(..., description="Correo electrónico del usuario")
    full_name: str = Field(..., description="Nombre completo del usuario")
    is_active: bool = Field(..., description="Estado de activación del usuario")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación")
