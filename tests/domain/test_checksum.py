import pytest
from app.services.pdf_service import PDFService

def test_checksum_consistency():
    """Verifica que el hash sea siempre el mismo para el mismo archivo."""
    content = b"contenido simulado de un pdf para utn"
    hash1 = PDFService.get_checksum(content)
    hash2 = PDFService.get_checksum(content)
    assert hash1 == hash2 # Tienen que ser idénticos

def test_extract_text_empty_pdf():
    """Verifica cómo reacciona el extractor ante un archivo corrupto o sin texto."""
    invalid_pdf_content = b"esto claramente no es un pdf valido"
    text = PDFService.extract_text(invalid_pdf_content)
    # Por ahora, nuestra lógica devuelve vacío si falla
    assert text == ""
    
from app.services.pdf_service import PDFService

def test_extract_text_from_scanned_pdf():
    """Test: Simula un PDF válido pero que no contiene texto seleccionable (ej. un escaneo)."""
    # Simulamos el contenido de un PDF que es solo imagen
    scanned_pdf_content = b"%PDF-1.4\n%...esto_es_una_imagen_sin_texto..."
    
    text = PDFService.extract_text(scanned_pdf_content)
    
    # Tiene que devolver string vacío, no un error
    assert text == ""
def test_extract_text_too_short():
    """Test: Verifica que el sistema no explote si recibe un archivo con 2 bytes de basura."""
    # Simulamos un contenido ridículamente corto que rompería un lector normal
    tiny_content = b"NO" 
    
    # Mandamos eso al extractor
    text = PDFService.extract_text(tiny_content)
    
    # Debe atajar el error y devolver un string vacío
    assert text == ""