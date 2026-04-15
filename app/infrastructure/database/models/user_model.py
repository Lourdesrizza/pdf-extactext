"""Modelo SQLAlchemy para Usuario."""
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.infrastructure.database.connection import Base


class UserModel(Base):
    """Modelo de base de datos para usuarios."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
