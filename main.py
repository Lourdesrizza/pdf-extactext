"""
================================================================================
ORQUESTADOR PRINCIPAL - main.py
================================================================================
Responsabilidad: Coordinar el flujo completo de extracción y procesamiento.
Equipo a cargo: Magallanes Angelina, Puente Maité, Rizza Lourdes, Roda Jeremias
Uso:
    python main.py <ruta_pdf> [ruta_salida]
================================================================================
"""
import logging
import sys
from pathlib import Path

from src.extractor import extract_text_from_pdf
from src.processor import clean_text, get_estadisticas, save_output

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Punto de entrada principal."""
    logger.info("=" * 80)
    logger.info("PDF-EXTACTEXT - Extracción de Texto de PDF")
    logger.info("=" * 80)

    argumentos: list[str] = sys.argv[1:]

    if len(argumentos) < 1:
        logger.error("Uso: python main.py <ruta_pdf> [ruta_salida]")
        sys.exit(1)

    ruta_pdf: str = argumentos[0]
    ruta_salida: Path = (
        Path(argumentos[1]) if len(argumentos) >= 2 else Path("resultado.txt")
    )

    logger.info("PDF: %s", ruta_pdf)
    logger.info("Salida: %s", ruta_salida)

    logger.info("[1/4] Extrayendo texto...")
    texto_crudo: str = extract_text_from_pdf(ruta_pdf)
    logger.info("%s caracteres extraídos", len(texto_crudo))

    logger.info("[2/4] Limpiando texto...")
    texto_limpio: str = clean_text(texto_crudo)
    logger.info("%s caracteres limpios", len(texto_limpio))

    logger.info("[3/4] Guardando resultado...")
    save_output(texto_limpio, ruta_salida, mostrar_consola=True)

    logger.info("[4/4] Estadísticas:")
    for clave, valor in get_estadisticas(texto_limpio).items():
        logger.info("%s: %s", clave.capitalize(), f"{valor:,}")

    logger.info("Completado")


if __name__ == "__main__":
    main()
