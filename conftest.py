# conftest.py  (raíz del proyecto)
import pytest
from unittest.mock import AsyncMock, MagicMock
from fastapi.testclient import TestClient

from app.main import app
from app.api.dependencies import get_document_repository, get_user_repository

@pytest.fixture
def mock_document_repo():
    repo = AsyncMock()
    repo.find_all.return_value = []
    repo.find_by_id.return_value = None
    repo.find_by_checksum.return_value = None
    return repo

@pytest.fixture
def mock_user_repo():
    repo = AsyncMock()
    repo.find_by_email.return_value = None
    repo.find_all.return_value = []
    return repo

@pytest.fixture
def client(mock_document_repo, mock_user_repo):
    """TestClient con MongoDB mockeado — no necesita Docker."""
    app.dependency_overrides[get_document_repository] = lambda: mock_document_repo
    app.dependency_overrides[get_user_repository] = lambda: mock_user_repo
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()