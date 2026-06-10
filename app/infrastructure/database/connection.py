# app/infrastructure/database/connection.py
from functools import lru_cache
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings

_client: AsyncIOMotorClient | None = None

def get_client() -> AsyncIOMotorClient:
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.DATABASE_URL)
    return _client

async def get_database_session() -> AsyncIOMotorDatabase:
    """Dependency para FastAPI — entrega la DB correcta según el .env."""
    yield get_client()[settings.DB_NAME]