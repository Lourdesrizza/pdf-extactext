"""
================================================================================
CAPA DE LÓGICA - src/processor.py
================================================================================
Responsabilidad: Limpiar, formatear y guardar el texto extraído.
Equipo a cargo: [Nombre del integrante de Lógica]
Este módulo contiene funciones para:
    - Limpiar espacios y saltos de línea innecesarios
    - Normalizar formato del texto
    - Guardar resultado en archivo TXT
    - Mostrar resultado por consola
================================================================================
"""
import re
from pathlib import Path
def clean_text(texto: str) -> str:
    """
    Limpia y formatea texto extraído de PDF.
    Operaciones:
        1. Elimina espacios múltiples
        2. Normaliza saltos de línea
        3. Une líneas fragmentadas de párrafos
        4. Elimina espacios al inicio/final
    Args:
        texto: Texto crudo extraído del PDF
    Returns:
        str: Texto limpio y formateado
    """
    if not texto:
        return ""
    texto_limpio: str = texto
    texto_limpio = texto_limpio.replace("\r\n", "\n")
    texto_limpio = texto_limpio.replace("\r", "\n")
    texto_limpio = re.sub(r"[ \t]+", " ", texto_limpio)
    lineas: list[str] = texto_limpio.split("\n")
    parrafos: list[str] = []
    bloque_actual: list[str] = []
    for linea in lineas:
        linea_stripped: str = linea.strip()
        if not linea_stripped:
            if bloque_actual:
                parrafo: str = " ".join(bloque_actual)
                parrafos.append(parrafo)
                bloque_actual = []
        elif not _es_fin_de_oracion(linea_stripped):
            bloque_actual.append(linea_stripped)
        else:
            if bloque_actual:
                parrafos.append(" ".join(bloque_actual))
            bloque_actual = [linea_stripped]
    if bloque_actual:
        parrafos.append(" ".join(bloque_actual))
    texto_limpio = "\n\n".join(parrafos)
    texto_limpio = re.sub(r"\n{3,}", "\n\n", texto_limpio)
    return texto_limpio.strip()
def _es_fin_de_oracion(linea: str) -> bool:
    """Determina si una línea termina en puntuación completa."""
    if not linea:
        return False
    return linea[-1] in {".", "!", "?", ":", ";", ","}
def save_output(
    texto: str,
    output_path: str | Path,
    mostrar_consola: bool = True
) -> None:
    """
    Guarda texto en archivo y opcionalmente lo muestra por consola.
    Args:
        texto: Texto a guardar
        output_path: Ruta del archivo de salida (.txt)
        mostrar_consola: Si True, imprime el texto en consola
    Raises:
        ValueError: Si output_path no tiene extensión .txt
        IOError: Si hay error al escribir el archivo
    """
    path = Path(output_path)
    if path.suffix.lower() != ".txt":
        raise ValueError(f"El archivo de salida debe ser .txt: {output_path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print(f"✓ Archivo guardado: {path.absolute()}")
    if mostrar_consola:
        print("\n" + "=" * 80)
        print("CONTENIDO EXTRAÍDO Y PROCESADO:")
        print("=" * 80)
        print(texto)
        print("=" * 80)
def get_estadisticas(texto: str) -> dict[str, int]:
    """Calcula estadísticas básicas del texto."""
    return {
        "caracteres": len(texto),
        "palabras": len(texto.split()),
        "lineas": len([l for l in texto.split("\n") if l.strip()]),
        "parrafos": len([p for p in texto.split("\n\n") if p.strip()]),
    }