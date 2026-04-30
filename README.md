```

---

##  Licencia
Este proyecto es desarrollado con fines académicos para la cátedra de **Desarrollo de Software** de la **Universidad Tecnológica Nacional - Facultad Regional San Rafael (UTN FRSR)**.

<div
```markdown
#  extracText — Extractor de Texto PDF

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688.svg?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4.7+-47A248.svg?style=for-the-badge&logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**Proyecto Académico — Desarrollo de Software (3er Año)**  
**UTN FRSR — 2026**

</div>

---

##  Descripción del Proyecto
**extracText** es una aplicación de extracción de texto de archivos PDF desarrollada siguiendo principios de arquitectura limpia y las mejores prácticas de ingeniería de software. El sistema permite:
- Extraer texto de archivos PDF de forma local (**CLI**) o remota (**API RESTful**).
- Procesar documentos directamente en memoria sin persistencia temporal.
- Almacenar metadatos y resultados en **MongoDB**.
- Detectar archivos duplicados mediante checksum **SHA256**.
- Limpiar y normalizar el texto extraído automáticamente.

---

##  Integrantes del Equipo
| Legajo | Nombre | Rol Principal |
|--------|--------|---------------|
| **10853** | Magallanes Angelina
| **10902** | Puente Maite
| **10913** | Rizza Lourdes
| **10917** | Roda Jeremias

**Cátedra:** Desarrollo de Software (3er Año - UTN FRSR - 2026)

---

##  Tecnologías y Librerías

### Core Framework
| Librería | Versión | Propósito |
|----------|---------|-----------|
| **FastAPI** | >=0.111.0 | Framework web asíncrono de alto rendimiento |
| **Motor** | >=3.7.1 | Driver asíncrono para MongoDB |
| **Pydantic** | >=2.7.0 | Validación de datos y esquemas |
| **UV** | - | Gestor de paquetes ultra-rápido |

### Procesamiento de PDFs
*   **PyMuPDF (fitz):** Utilizado en la API para lectura directa desde memoria sin persistencia temporal.
*   **pypdf:** Utilizado en el módulo CLI por su simplicidad y velocidad local.
*   **Opcionales:** `pdfplumber` (tablas) y `Tesseract OCR` (escaneados).

---

##  Arquitectura del Sistema

### Capas del Sistema (Clean Architecture)
El proyecto sigue una arquitectura en **4 capas** bien separadas, comunicadas a través de interfaces abstractas:

1.  **Presentation Layer (API/CLI):** Routers de FastAPI y puntos de entrada de consola.
2.  **Application Layer (Services):** Orquestación de lógica, DTOs y casos de uso.
3.  **Domain Layer (Entities):** Reglas de negocio puras, modelos y definiciones de repositorios.
4.  **Infrastructure Layer (Persistence):** Implementación concreta de MongoDB y librerías de terceros.

### Principios de Ingeniería Aplicados
*   **12-Factor App:** Configuración externalizada (`.env`), gestión de dependencias aisladas y procesos sin estado.
*   **SOLID:** Responsabilidad única, código abierto/cerrado e inversión de dependencias.
*   **Clean Code:** Aplicación de **DRY** (Don't Repeat Yourself), **KISS** (Keep It Simple) y **YAGNI**.

---

##  Instalación y Configuración

### Requisitos Previos
- Python 3.12+
- [UV](https://github.com/astral-sh/uv) (Gestor de paquetes)
- Docker Desktop (para MongoDB)

### Paso 1: Clonar y Configurar
```bash
git clone https://github.com/TU_USUARIO/extracText.git
cd extracText
copy .env.example .env
```

### Paso 2: Instalación de Dependencias
```bash
# Instalación rápida con uv
uv sync --all-extras
```

### Paso 3: Levantar Base de Datos
```bash
# Iniciar contenedor de MongoDB
docker run -d -p 27017:27017 --name mongo mongo:7
```

### Paso 4: Ejecución
*   **Modo API:** `uv run uvicorn app.main:app --reload`  
    *Documentación Swagger: http://localhost:8000/docs*
*   **Modo CLI:** `python main.py "archivo.pdf" "salida.txt"`

---

##  Estructura del Proyecto
```text
pdf-extactext/
├── app/                # Aplicación API (Capa de arquitectura)
│   ├── api/            # Capa Presentación (Routers)
│   ├── application/    # Capa Aplicación (Servicios/DTOs)
│   ├── domain/         # Capa Dominio (Entidades/Interfaces)
│   └── infrastructure/ # Capa Infraestructura (DB/Schemas)
├── src/                # Scripts standalone (CLI)
├── tests/              # Suite de pruebas con Pytest
├── main.py             # Entry point CLI
└── pyproject.toml      # Dependencias y configuración
```

---

##  Testing y Calidad
```bash
# Ejecutar todos los tests automatizados
uv run pytest

# Con reporte de cobertura
uv run pytest --cov=app --cov=src
```

---

##  Licencia
Este proyecto es desarrollado con fines académicos para la cátedra de **Desarrollo de Software** de la **Universidad Tecnológica Nacional - Facultad Regional San Rafael (UTN FRSR)**.

<div align="center">

**UTN FRSR — Ingeniería en Sistemas de Información — 2026**

[ ⬆ Volver al inicio ](#-extractext--extractor-de-texto-pdf)

</div>
```

```