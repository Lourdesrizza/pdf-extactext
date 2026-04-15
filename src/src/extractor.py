"""
================================================================================
CAPA DE DATOS - src/extractor.py
================================================================================
Responsabilidad: Leer archivos PDF y extraer texto plano.
Equipo a cargo: [Nombre del integrante de Datos]
Este módulo contiene funciones para:
    - Abrir archivos PDF usando pypdf
    - Extraer texto página por página
    - Retornar texto crudo para ser procesado
================================================================================
"""
from pathlib import Path
from typing import Optional
from pypdf import PdfReader
def extract_text_from_pdf(file_path: str | Path) -> str:
    """
    Extrae todo el texto de un archivo PDF.
    Args:
        file_path: Ruta al archivo PDF (str o Path)
    Returns:
        str: Texto completo extraído del PDF
    Raises:
        FileNotFoundError: Si el archivo PDF no existe
        ValueError: Si el archivo no es un PDF
        Exception: Si hay error al leer el PDF
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
    if not path.suffix.lower() == ".pdf":
        raise ValueError(f"El archivo debe ser un PDF: {file_path}")
    texto_completo: list[str] = []
    try:
        reader = PdfReader(path)
        for pagina in reader.pages:
            texto_pagina: Optional[str] = pagina.extract_text()
            if texto_pagina:
                texto_completo.append(texto_pagina)
        return "\n\n".join(texto_completo)
    except Exception as e:
        raise Exception(f"Error al leer el PDF: {e}") from e
def extract_text_from_pdf_by_page(
    file_path: str | Path
) -> list[tuple[int, str]]:
    """
    Extrae texto de un PDF página por página.
    Args:
        file_path: Ruta al archivo PDF (str o Path)
    Returns:
        list[tuple[int, str]]: Lista de tuplas (número_página, texto)
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
    resultado: list[tuple[int, str]] = []
    try:
        reader = PdfReader(path)
        for numero_pagina, pagina in enumerate(reader.pages, start=1):
            texto: Optional[str] = pagina.extract_text()
            if texto:
                resultado.append((numero_pagina, texto))
        return resultado
    except Exception as e:
        raise Exception(f"Error al leer el PDF página por página: {e}") from e