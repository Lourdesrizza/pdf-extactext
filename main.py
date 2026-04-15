"""
================================================================================
ORQUESTADOR PRINCIPAL - main.py
================================================================================
Responsabilidad: Coordinar el flujo completo de extracción y procesamiento.
Equipo a cargo: [Nombre del integrante de Orquestación]
Uso:
    python main.py <ruta_pdf> [ruta_salida]
================================================================================
"""
import sys
from pathlib import Path
from src.extractor import extract_text_from_pdf
from src.processor import clean_text, get_estadisticas, save_output
def main() -> None:
    """Punto de entrada principal."""
    print("=" * 80)
    print("PDF-EXTACTEXT - Extracción de Texto de PDF")
    print("=" * 80)
    argumentos: list[str] = sys.argv[1:]
    if len(argumentos) < 1:
        print("\nUso: python main.py <ruta_pdf> [ruta_salida]")
        sys.exit(1)
    ruta_pdf: str = argumentos[0]
    ruta_salida: Path = (
        Path(argumentos[1]) if len(argumentos) >= 2 else Path("resultado.txt")
    )
    print(f"\n PDF: {ruta_pdf}")
    print(f" Salida: {ruta_salida}")
    print("\n[1/4] Extrayendo texto...")
    texto_crudo: str = extract_text_from_pdf(ruta_pdf)
    print(f"   ✓ {len(texto_crudo)} caracteres extraídos")
    print("\n[2/4] Limpiando texto...")
    texto_limpio: str = clean_text(texto_crudo)
    print(f"   ✓ {len(texto_limpio)} caracteres limpios")
    print("\n[3/4] Guardando resultado...")
    save_output(texto_limpio, ruta_salida, mostrar_consola=True)
    print("\n[4/4] Estadísticas:")
    for clave, valor in get_estadisticas(texto_limpio).items():
        print(f"   • {clave.capitalize()}: {valor:,}")
    print("\n✓ Completado")
if __name__ == "__main__":
    main()