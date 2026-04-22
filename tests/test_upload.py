import pytest
from fastapi.testclient import TestClient
from app.main import app  # Importamos tu aplicación

client = TestClient(app)

def test_upload_pdf_success():
    """Prueba que un archivo PDF válido sea aceptado."""
    # Creamos un "falso" archivo PDF en memoria
    file_content = b"%PDF-1.4 dummy content"
    files = {"file": ("test.pdf", file_content, "application/pdf")}
    
    response = client.post("/api/v1/upload", files=files)
    
    assert response.status_code == 200
    assert response.json()["filename"] == "test.pdf"

def test_upload_invalid_format():
    """Prueba que un archivo que NO es PDF sea rechazado (Error 400)."""
    file_content = b"esto es un texto plano"
    files = {"file": ("test.txt", file_content, "text/plain")}
    
    response = client.post("/api/v1/upload", files=files)
    
    # Según tu consigna, esto debería fallar con 400
    assert response.status_code == 400
    assert response.json()["detail"] == "El archivo debe ser un PDF"

def test_upload_no_file():
    """Prueba qué pasa si no se envía ningún archivo."""
    response = client.post("/api/v1/upload")
    
    # FastAPI devuelve 422 (Unprocessable Entity) automáticamente si falta el archivo
    assert response.status_code == 422