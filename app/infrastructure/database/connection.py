"""Configuración de conexión a base de datos MongoDB."""

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings

_client: AsyncIOMotorClient | None = None


def get_client() -> AsyncIOMotorClient:
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.DATABASE_URL)
    return _client


async def get_database_session() -> AsyncIOMotorDatabase:
    yield get_client()[settings.DB_NAME]