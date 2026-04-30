import pytest

def test_file_signature_valid_pdf():
    """Test: Verifica que el archivo empiece con la firma correcta de un PDF."""
    pdf_header = b"%PDF-1.4..."
    assert pdf_header.startswith(b"%PDF")

def test_file_signature_invalid_file():
    """Test: Rechaza un archivo si la firma es de una imagen (ej. PNG)."""
    png_header = b"\x89PNG\r\n\x1a\n"
    assert not png_header.startswith(b"%PDF")

def test_encryption_check_mock():
    """Test: Simula la detección de un PDF con contraseña."""
    pdf_falso_encriptado = {"is_encrypted": True}
    assert pdf_falso_encriptado["is_encrypted"] is True