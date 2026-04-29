"""Configuración de conexión a base de datos MongoDB."""
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# 1. Creamos el cliente de MongoDB conectado a la URL de tus settings
client = AsyncIOMotorClient(settings.DATABASE_URL)

# 2. Seleccionamos el nombre de tu base de datos (podés cambiar "pdf_extractor_db" al nombre que quieras)
database = client.pdf_extractor_db

# 3. Hacemos la función asíncrona porque Motor trabaja de forma no bloqueante
async def get_database_session():
    """Generador de conexión a la base de datos MongoDB para FastAPI."""
    try:
        # En MongoDB, simplemente entregamos la base de datos entera
        yield database
    finally:
        # Nota: Motor maneja el cierre de conexiones automáticamente mediante un "pool".
        # No necesitamos cerrar la sesión en cada request como hacíamos en SQL.
        pass
