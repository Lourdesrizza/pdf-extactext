"""Interfaz del repositorio de documentos."""

from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.document import Document


class DocumentRepository(ABC):
    """Contrato para operaciones de persistencia de documentos.

    Esta interfaz es agnóstica a la implementación de base de datos.
    Todos los métodos son async para soportar operaciones no bloqueantes.
    Los IDs son strings para soportar MongoDB ObjectId.
    """

    @abstractmethod
    async def find_by_id(self, document_id: str) -> Optional[Document]:
        """Busca un documento por su ID.

        Args:
            document_id: ID del documento como string.

        Returns:
            Entidad Document si existe, None si no se encuentra.
        """
        raise NotImplementedError

    @abstractmethod
    async def find_by_checksum(self, checksum: str) -> Optional[Document]:
        """Busca un documento por su checksum.

        Args:
            checksum: Hash SHA256 del contenido.

        Returns:
            Entidad Document si existe, None si no se encuentra.
        """
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> List[Document]:
        """Obtiene todos los documentos.

        Returns:
            Lista de entidades Document.
        """
        raise NotImplementedError

    @abstractmethod
    async def create(self, document: Document) -> Document:
        """Crea un nuevo documento.

        Args:
            document: Entidad Document a crear.

        Returns:
            Entidad Document creada con ID asignado.
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, document: Document) -> Document:
        """Actualiza un documento existente (solo filename es mutable).

        Args:
            document: Entidad Document con datos actualizados.

        Returns:
            Entidad Document actualizada.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, document_id: str) -> None:
        """Elimina un documento por su ID.

        Args:
            document_id: ID del documento a eliminar.
        """
        raise NotImplementedError
