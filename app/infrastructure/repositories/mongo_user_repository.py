"""Implementación MongoDB del repositorio de usuarios."""

from typing import List, Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.schemas.user_schema import (
    UserCreate,
    UserInDB,
    UserUpdate,
)


class MongoUserRepository(UserRepository):
    """Repositorio de usuarios usando MongoDB con Motor."""

    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        """Inicializa el repositorio con la colección de usuarios.

        Args:
            database: Instancia de base de datos MongoDB de Motor.
        """
        self._collection = database.users

    async def find_by_id(self, user_id: str) -> Optional[User]:
        """Busca un usuario por su ID.

        Args:
            user_id: ID del usuario como string.

        Returns:
            Entidad User si existe, None si no se encuentra.
        """
        try:
            document = await self._collection.find_one({"_id": ObjectId(user_id)})
            if document:
                return self._to_entity(UserInDB.model_validate(document))
            return None
        except Exception:
            return None

    async def find_by_email(self, email: str) -> Optional[User]:
        """Busca un usuario por su email.

        Args:
            email: Email del usuario.

        Returns:
            Entidad User si existe, None si no se encuentra.
        """
        document = await self._collection.find_one({"email": email.lower().strip()})
        if document:
            return self._to_entity(UserInDB.model_validate(document))
        return None

    async def find_all(self) -> List[User]:
        """Obtiene todos los usuarios.

        Returns:
            Lista de entidades User.
        """
        users = []
        cursor = self._collection.find()
        async for document in cursor:
            users.append(self._to_entity(UserInDB.model_validate(document)))
        return users

    async def create(self, user: User) -> User:
        """Crea un nuevo usuario.

        Args:
            user: Entidad User a crear.

        Returns:
            Entidad User creada con ID asignado.
        """
        user_create = UserCreate(
            email=user.email,
            full_name=user.full_name,
            is_active=user.is_active,
        )

        user_in_db = UserInDB(**user_create.model_dump())
        document = user_in_db.model_dump(by_alias=True, exclude={"id"})

        result = await self._collection.insert_one(document)
        user_in_db.id = str(result.inserted_id)

        return self._to_entity(user_in_db)

    async def update(self, user: User) -> User:
        """Actualiza un usuario existente.

        Args:
            user: Entidad User con datos actualizados.

        Returns:
            Entidad User actualizada.
        """
        from datetime import datetime

        if not user.id:
            raise ValueError("El usuario debe tener un ID para actualizarse")

        update_data = {
            "full_name": user.full_name,
            "is_active": user.is_active,
            "updated_at": datetime.utcnow(),
        }

        await self._collection.update_one(
            {"_id": ObjectId(user.id)}, {"$set": update_data}
        )

        return user

    async def delete(self, user_id: str) -> None:
        """Elimina un usuario por su ID.

        Args:
            user_id: ID del usuario a eliminar.
        """
        await self._collection.delete_one({"_id": ObjectId(user_id)})

    def _to_entity(self, user_in_db: UserInDB) -> User:
        """Convierte schema Pydantic a entidad de dominio.

        Args:
            user_in_db: Schema UserInDB.

        Returns:
            Entidad User del dominio.
        """
        return User(
            id=user_in_db.id,
            email=user_in_db.email,
            full_name=user_in_db.full_name,
            is_active=user_in_db.is_active,
            created_at=user_in_db.created_at,
        )
