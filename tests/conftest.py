import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Esta fixture permite usar el cliente de pruebas en cualquier archivo de test."""
    return TestClient(app)