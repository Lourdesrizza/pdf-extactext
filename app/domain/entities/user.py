"""Entidad Usuario del dominio."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    """Representa un usuario en el sistema."""

    id: Optional[int] = None
    email: str = ""
    full_name: str = ""
    is_active: bool = True
    created_at: Optional[datetime] = None

    def activate(self) -> None:
        """Activa la cuenta del usuario."""
        self.is_active = True

    def deactivate(self) -> None:
        """Desactiva la cuenta del usuario."""
        self.is_active = False

    def update_profile(self, full_name: str) -> None:
        """Actualiza el nombre completo del usuario."""
        self.full_name = full_name
