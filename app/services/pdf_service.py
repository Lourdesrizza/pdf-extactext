import hashlib
import fitz  # PyMuPDF
from io import BytesIO

class PDFService:
    @staticmethod
    def get_checksum(content: bytes) -> str:
        """Genera un hash SHA256 para identificar archivos duplicados."""
        return hashlib.sha256(content).hexdigest()

    @staticmethod
    def extract_text(content: bytes) -> str:
        """Extrae solamente el texto del PDF desde la memoria (sin guardarlo en disco)."""
        text = ""
        # Abrimos el PDF desde los bytes en memoria (Requerimiento de no persistir temporalmente)
        with fitz.open(stream=content, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text.strip()