import pytest
from app.services.pdf_service import PDFService

def test_checksum_consistency():
    """Verifica que el hash sea siempre igual para el mismo contenido."""
    content = b"contenido de prueba para hash"
    hash1 = PDFService.get_checksum(content)
    hash2 = PDFService.get_checksum(content)
    assert hash1 == hash2

def test_extract_text_logic():
    """Verifica que la extracción devuelva vacío si el PDF es inválido."""
    invalid_content = b"esto no es un pdf real"
    text = PDFService.extract_text(invalid_content)
    assert text == ""