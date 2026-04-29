"""Entidad Usuario del dominio."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class User:
    """Representa un usuario en el sistema.

    Esta entidad de dominio es agnóstica a la base de datos.
    El ID es un string para soportar MongoDB ObjectId.
    """

    id: Optional[str] = None
    email: str = ""
    full_name: str = ""
    is_active: bool = True
    created_at: Optional[datetime] = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        """Validaciones post-inicialización."""
        if self.email:
            self.email = self.email.lower().strip()
        if self.full_name:
            self.full_name = self.full_name.strip()

    def activate(self) -> None:
        """Activa la cuenta del usuario."""
        self.is_active = True

    def deactivate(self) -> None:
        """Desactiva la cuenta del usuario."""
        self.is_active = False

    def update_profile(self, full_name: str) -> None:
        """Actualiza el nombre completo del usuario.

        Args:
            full_name: Nuevo nombre completo (se limpia automáticamente).
        """
        self.full_name = full_name.strip()

    def __eq__(self, other: object) -> bool:
        """Compara usuarios por su ID."""
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        """Hash basado en el ID para usar en colecciones."""
        return hash(self.id)
