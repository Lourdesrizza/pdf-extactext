"""DTOs para transferencia de datos de usuarios."""
from pydantic import BaseModel, EmailStr


class UserCreateRequest(BaseModel):
    """DTO para crear un usuario."""

    email: EmailStr
    full_name: str


class UserUpdateRequest(BaseModel):
    """DTO para actualizar un usuario."""

    full_name: str


class UserResponse(BaseModel):
    """DTO para respuesta de usuario."""

    id: int
    email: str
    full_name: str
    is_active: bool

    class Config:
        from_attributes = True
