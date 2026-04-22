from pydantic_settings import BaseSettings, SettingsConfigDict

class ApplicationSettings(BaseSettings):
    """Configuración central de la aplicación."""
    
    # Estos nombres deben matchear con tu archivo .env
    API_V1_STR: str
    DEBUG: bool
    DATABASE_URL: str
    DB_NAME: str
    SECRET_KEY: str

    # Esta es la forma moderna (Pydantic V2) de cargar el .env
    model_config = SettingsConfigDict(env_file=".env")

# Instanciamos para que el resto de la app lo use
settings = ApplicationSettings()