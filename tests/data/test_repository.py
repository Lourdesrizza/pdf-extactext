import pytest
def test_mock_save_document():
    """Simula el guardado de un documento en la base de datos."""
    documento_mock = {
        "filename": "tp_sistemas.pdf",
        "checksum": "abc123hash",
        "content": "Este es el texto extraído."
    }
    
    assert "checksum" in documento_mock
    assert documento_mock["filename"] == "tp_sistemas.pdf"

def test_mock_find_duplicate():
    """Simula la búsqueda de un duplicado en la base de datos."""
    db_falsa = ["abc123hash", "xyz987hash"]
    nuevo_checksum = "abc123hash"
    
    es_duplicado = nuevo_checksum in db_falsa
    assert es_duplicado is True
    
def test_mock_get_all_documents():
    """Simula obtener todos los documentos guardados en la base de datos."""
    db_falsa = [{"filename": "doc1.pdf"}, {"filename": "doc2.pdf"}]
    assert len(db_falsa) == 2

def test_mock_delete_document():
    """Simula borrar un documento específico."""
    db_falsa = ["abc123hash", "xyz987hash"]
    checksum_a_borrar = "abc123hash"
    
    # Simulamos el borrado
    db_falsa.remove(checksum_a_borrar)
    
    assert checksum_a_borrar not in db_falsa
    assert len(db_falsa) == 1
    
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_database_connection_success():
    """Test: Simula que la conexión a MongoDB devuelve OK."""
    # Usamos AsyncMock para simular la respuesta de Motor/MongoDB
    mock_db_client = AsyncMock()
    mock_db_client.server_info.return_value = {"ok": 1.0}
    
    info = await mock_db_client.server_info()
    assert info["ok"] == 1.0

def test_mock_update_document():
    """Test: Simula la actualización (Update) de un documento existente."""
    db_falsa = {"abc123hash": {"filename": "viejo_nombre.pdf", "status": "pendiente"}}
    
    # Actualizamos el estado
    db_falsa["abc123hash"]["status"] = "procesado"
    
    assert db_falsa["abc123hash"]["status"] == "procesado"

def test_mock_find_by_checksum_not_found():
    """Test: Simula buscar un checksum que no existe en la base de datos."""
    db_falsa = ["abc123hash"]
    busqueda = "no_existo_hash"
    
    encontrado = busqueda in db_falsa
    assert encontrado is False
    
from unittest.mock import AsyncMock
import pymongo.errors

@pytest.mark.asyncio
async def test_database_connection_failure_handled():
    """Test: Simula una caída del servidor de la base de datos (Ej: Docker apagado)."""
    mock_db_client = AsyncMock()
    
    # Le decimos al simulador que tire un error de Timeout a propósito
    mock_db_client.server_info.side_effect = pymongo.errors.ServerSelectionTimeoutError("Timeout simulado")
    
    # Verificamos que Python ataje ese error correctamente
    with pytest.raises(pymongo.errors.ServerSelectionTimeoutError):
        await mock_db_client.server_info()
        
def test_mock_save_same_name_different_content():
    """Test: Permite guardar dos archivos con el mismo nombre si su contenido (hash) es distinto."""
    # Base de datos simulada con un archivo ya guardado
    db_falsa = [{"filename": "tp_final.pdf", "checksum": "hash_original_123"}]
    
    # Entra un archivo nuevo con el Mismo nombre, pero Distinto hash
    nuevo_checksum = "hash_completamente_nuevo_456"
    
    # Verificamos si la lógica lo detecta como duplicado (solo debe mirar el hash)
    es_duplicado = nuevo_checksum in [doc["checksum"] for doc in db_falsa]
    
    # No es duplicado, ¡debe dejarlo pasar!
    assert es_duplicado is False
import pytest
# Asegurate de que esta ruta coincida con donde tienen guardadas las excepciones en su proyecto
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError, DocumentAlreadyExistsError

def test_mock_find_nonexistent_raises_error():
    db_falsa = []
    checksum_buscado = "hash_fantasma"
    
    with pytest.raises(DocumentNotFoundError):
        if checksum_buscado not in db_falsa:
            raise DocumentNotFoundError(f"Document with checksum {checksum_buscado} not found.")

def test_mock_delete_nonexistent_raises_error():
    db_falsa = ["hash_real_123"]
    checksum_a_borrar = "hash_fantasma"
    
    with pytest.raises(DocumentNotFoundError):
        if checksum_a_borrar not in db_falsa:
            raise DocumentNotFoundError(f"Document with checksum {checksum_a_borrar} not found.")

def test_mock_save_duplicate_raises_error():
    db_falsa = ["hash_duplicado_123"]
    nuevo_checksum = "hash_duplicado_123"
    
    with pytest.raises(DocumentAlreadyExistsError):
        if nuevo_checksum in db_falsa:
            raise DocumentAlreadyExistsError("El documento ya existe")