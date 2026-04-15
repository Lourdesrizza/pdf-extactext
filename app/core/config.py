"""Configuración de la aplicación."""
from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    """Configuración central de la aplicación."""

    app_name: str = "Clean API"
    debug_mode: bool = False
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "your-secret-key-here"

    class Config:
        env_file = ".env"


settings = ApplicationSettings()
