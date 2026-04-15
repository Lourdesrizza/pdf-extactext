"""
src package - Módulo principal del proyecto pdf-extactext
Estructura de paquetes:
    - extractor.py: Capa de Datos (lectura de PDFs)
    - processor.py: Capa de Lógica (procesamiento de texto)
"""
from .extractor import extract_text_from_pdf
from .processor import clean_text, save_output
__all__ = ["extract_text_from_pdf", "clean_text", "save_output"]