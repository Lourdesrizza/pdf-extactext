"""Schemas Pydantic para documentos con validación MongoDB."""

from datetime import datetime
from typing import Annotated, Optional

from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, field_validator


PyObjectId = Annotated[str, BeforeValidator(str)]


class DocumentBase(BaseModel):
    """Schema base para documentos con campos comunes."""

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )

    filename: str = Field(
        ..., min_length=1, max_length=255, description="Nombre del archivo"
    )
    checksum: str = Field(
        ...,
        min_length=64,  # SHA256:64 hex characters
        max_length=64,
        description="Hash SHA256 del contenido",
    )
    extracted_text: str = Field(..., description="Texto extraído del archivo PDF")

    @field_validator("filename")
    @classmethod
    def validate_filename(cls, value: str) -> str:
        """Valida que el nombre del archivo no esté vacío y se limpie."""
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("El nombre del archivo no puede estar vacío")
        return cleaned


class DocumentCreate(DocumentBase):
    """Schema para crear un nuevo documento."""

    pass


class DocumentUpdate(BaseModel):
    """Schema para actualizar un documento existente (solo filename).

    Nota: checksum y extracted_text son inmutables.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )

    filename: Optional[str] = Field(
        None, min_length=1, max_length=255, description="Nuevo nombre del archivo"
    )

    @field_validator("filename")
    @classmethod
    def validate_filename(cls, value: Optional[str]) -> Optional[str]:
        """Valida que el nombre del archivo no esté vacío si se proporciona."""
        if value is not None:
            cleaned = value.strip()
            if not cleaned:
                raise ValueError("El nombre del archivo no puede estar vacío")
            return cleaned
        return value


class DocumentInDB(DocumentBase):
    """Schema que representa un documento almacenado en MongoDB.

    Incluye el ID generado por MongoDB y timestamp de creación.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )

    id: PyObjectId = Field(
        default_factory=lambda: str(ObjectId()),
        alias="_id",
        description="ID único de MongoDB",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="Fecha de creación"
    )


class DocumentResponse(BaseModel):
    """Schema para respuestas de API."""

    id: str = Field(..., description="ID único del documento")
    filename: str = Field(..., description="Nombre del archivo")
    checksum: str = Field(..., description="Hash SHA256 del contenido")
    extracted_text: str = Field(..., description="Texto extraído del archivo PDF")
    created_at: Optional[datetime] = Field(
        default=None, description="Fecha de creación"
    )

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )
