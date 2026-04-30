import pytest
import fitz 



def test_upload_pdf(client):  # <-- TIENE QUE DECIR 'client', NO 'cliente'
    """Test: Subida de PDF real con texto."""
    doc = fitz.open()
    page = doc.new_page() 
    page.insert_text((50, 50), "Probando la API")
    pdf_bytes = doc.write()
    
    files = {"file": ("test.pdf", pdf_bytes, "application/pdf")}
    # Usamos 'client' (el nombre del parámetro)
    response = client.post("/api/v1/upload", files=files)
    
    assert response.status_code == 200
    assert "checksum" in response.json()

def test_upload_invalid_format(client): # <-- AGREGAMOS '(client)' ACÁ TAMBIÉN
    """Test: Rechazo de archivos TXT."""
    file_content = b"esto es texto"
    files = {"file": ("test.txt", file_content, "text/plain")}
    
    response = client.post("/api/v1/upload", files=files)
    
    assert response.status_code == 400
    assert response.json()["detail"] == "El archivo debe ser un PDF"
    
def test_upload_file_too_large(client):
    """Test: Simula el rechazo de un archivo que supera el límite de 5MB."""
    # Creamos un archivo falso pesado
    large_content = b"0" * (6 * 1024 * 1024) # 6 MB de ceros
    files = {"file": ("pesado.pdf", large_content, "application/pdf")}
    
    response = client.post("/api/v1/upload", files=files)
    
    # Dependiendo de cómo lo configuraste, FastAPI podría cortar la conexión 
    # o devolver un 413 (Payload Too Large) o 400.
    assert response.status_code in [400, 413, 422]

def test_api_health_check(client):
    """Test: Verifica que el servidor de FastAPI esté vivo y respondiendo."""
    response = client.get("/") # O la ruta de health que tengan
    assert response.status_code in [200, 404] # Al menos sabemos que el server responde
    
def test_upload_image_instead_of_pdf(client):
    """Test: Verifica qué pasa si el usuario intenta subir una imagen (PNG)."""
    # Simulamos el encabezado de un archivo de imagen real
    fake_image_content = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR..."
    files = {"file": ("foto_amarillo.png", fake_image_content, "image/png")}
    
    response = client.post("/api/v1/upload", files=files)
    
    # La API debería rebotarlo por el formato
    assert response.status_code == 400
    assert "PDF" in response.json()["detail"] # Asegura que el mensaje avise que debe ser PDF
    
def test_upload_empty_file_0_bytes(client):
    """Test: Verifica que la API rechace un PDF que pesa 0 bytes."""
    # Le mandamos b"" (bytes vacíos)
    files = {"file": ("vacio.pdf", b"", "application/pdf")}
    response = client.post("/api/v1/upload", files=files)
    
    # Debe tirar error de validación o Bad Request
    assert response.status_code in [400, 422]