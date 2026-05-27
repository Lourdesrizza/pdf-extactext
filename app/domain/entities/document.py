"""Entidad Documento del dominio."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Document:
    """Representa un documento en el sistema.

    Esta entidad de dominio es agnóstica a la base de datos.
    El ID es un string para soportar MongoDB ObjectId.
    Los campos checksum y extracted_text son inmutables una vez creados.
    """

    id: Optional[str] = None
    filename: str = ""
    """Nombre del archivo (mutable a través de update)."""
    checksum: str = field(default="", repr=False)
    """Hash SHA256 del contenido (inmutable después de la creación)."""
    extracted_text: str = field(default="", repr=False)
    """Texto extraído del archivo PDF (inmutable después de la creación)."""
    created_at: Optional[datetime] = field(default_factory=datetime.utcnow)
    """Fecha de creación del documento."""

    def __post_init__(self):
        """Validaciones post-inicialización."""
        if self.filename:
            self.filename = self.filename.strip()

    def update_filename(self, new_filename: str) -> None:
        """Actualiza el nombre del archivo.

        Args:
            new_filename: Nuevo nombre del archivo (se limpia automáticamente).

        Raises:
            ValueError: Si new_filename es vacío o solo contiene espacios.
        """
        cleaned = new_filename.strip()
        if not cleaned:
            raise ValueError("El nombre del archivo no puede estar vacío")
        self.filename = cleaned

    def __eq__(self, other: object) -> bool:
        """Compara documentos por su ID."""
        if not isinstance(other, Document):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        """Hash basado en el ID para usar en colecciones."""
        return hash(self.id)
