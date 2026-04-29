"""Schemas Pydantic para usuarios con validación MongoDB."""

from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class PyObjectId(ObjectId):
    """Clase helper para validar ObjectId de MongoDB."""

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        """Define el schema de validación para Pydantic."""
        from pydantic_core import core_schema

        return core_schema.no_info_plain_validator_function(
            cls.validate,
            core_schema.str_schema(),
        )

    @classmethod
    def validate(cls, value):
        """Valida que el valor sea un ObjectId válido."""
        if not ObjectId.is_valid(value):
            raise ValueError("ID de MongoDB inválido")
        return str(value)


class UserBase(BaseModel):
    """Schema base para usuarios con campos comunes."""

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )

    email: EmailStr = Field(..., description="Correo electrónico del usuario")
    full_name: str = Field(
        ..., min_length=1, max_length=255, description="Nombre completo del usuario"
    )
    is_active: bool = Field(
        default=True, description="Estado de activación del usuario"
    )

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, value: str) -> str:
        """Valida que el nombre no esté vacío y se limpie."""
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("El nombre completo no puede estar vacío")
        return cleaned


class UserCreate(UserBase):
    """Schema para crear un nuevo usuario."""

    pass


class UserUpdate(BaseModel):
    """Schema para actualizar un usuario existente."""

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )

    full_name: Optional[str] = Field(
        None, min_length=1, max_length=255, description="Nombre completo del usuario"
    )
    is_active: Optional[bool] = Field(
        None, description="Estado de activación del usuario"
    )

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, value: Optional[str]) -> Optional[str]:
        """Valida que el nombre no esté vacío si se proporciona."""
        if value is not None:
            cleaned = value.strip()
            if not cleaned:
                raise ValueError("El nombre completo no puede estar vacío")
            return cleaned
        return value


class UserInDB(UserBase):
    """Schema que representa un usuario almacenado en MongoDB.

    Incluye el ID generado por MongoDB y timestamps.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )

    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        alias="_id",
        description="ID único de MongoDB",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="Fecha de creación"
    )
    updated_at: Optional[datetime] = Field(
        default=None, description="Fecha de última actualización"
    )


class UserResponse(UserInDB):
    """Schema para respuestas de API.

    Extiende UserInDB sin modificaciones adicionales,
    pero puede usarse para campos de solo lectura en el futuro.
    """

    pass


class UserFilter(BaseModel):
    """Schema para filtrar usuarios en consultas."""

    model_config = ConfigDict(
        populate_by_name=True,
    )

    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
