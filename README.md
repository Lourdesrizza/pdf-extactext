# extracText - Extractor de texto PDF
<div align="center">
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-4.7+-47A248.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
**Proyecto Académico - Desarrollo de Software (3er Año)**
**UTN FRSR - 2026**
</div>
---
## Tabla de Contenidos
1. [Descripción del Proyecto](#-descripción-del-proyecto)
2. [Integrantes del Equipo](#-integrantes-del-equipo)
3. [Tecnologías y Librerías](#-tecnologías-y-librerías)
4. [Arquitectura del Sistema](#-arquitectura-del-sistema)
5. [Principios de Ingeniería de Software](#-principios-de-ingeniería-de-software)
6. [Instalación y Configuración](#-instalación-y-configuración)
7. [Uso de la Aplicación](#-uso-de-la-aplicación)
8. [Estructura del Proyecto](#-estructura-del-proyecto)
9. [API Endpoints](#-api-endpoints)
10. [Licencia](#-licencia)
---
##  Descripción del Proyecto
**extracText** es una aplicación de extracción de texto de archivos PDF desarrollada siguiendo principios de arquitectura limpia y las mejores prácticas de ingeniería de software. El sistema permite:
-  Extraer texto de archivos PDF de forma local (CLI)
-  Procesar PDFs mediante API RESTful
-  Almacenar metadatos y resultados en MongoDB
-  Detectar archivos duplicados mediante checksum SHA256
-  Limpiar y normalizar texto extraído
---
##  Integrantes del Equipo
| Legajo | Nombre | Rol Principal |
|--------|--------|---------------|
| **10939** | Sirotiuk Juliana | Domain Layer & Entities |
| **10842** | Jamardo Camila | Application Layer & Services |
| **10882** | Ojeda Tomas | Infrastructure & API Layer |
**Cátedra:** Desarrollo de Software (3er Año - UTN FRSR - 2026)
---
##  Tecnologías y Librerías
### Core Framework
| Librería | Versión | Propósito |
|----------|---------|-----------|
| **FastAPI** | >=0.111.0 | Framework web asíncrono de alto rendimiento |
| **Uvicorn** | >=0.30.0 | Servidor ASGI para ejecutar la aplicación |
| **Pydantic** | >=2.7.0 | Validación de datos y serialización |
| **Pydantic-Settings** | >=2.2.1 | Gestión de configuración mediante variables de entorno |
### Procesamiento de PDFs
| Librería | Versión | Cuándo Usar |
|----------|---------|-------------|
| **pypdf** | >=6.10.1 | PDFs con texto nativo digital (más rápido) |
| **PyMuPDF (fitz)** | >=1.27.2.2 | PDFs complejos, necesidad de lectura en memoria |
| **pdfplumber** | - | Tablas y estructuras complejas (opcional) |
| **Tesseract OCR** | - | PDFs escaneados (requiere imagen a texto) |
> ** Decisión de Diseño:** Usamos `pypdf` para extracción local por simplicidad y `PyMuPDF` en la API para lectura directa desde memoria sin persistencia temporal.
### Base de Datos
| Librería | Versión | Propósito |
|----------|---------|-----------|
| **Motor** | >=3.7.1 | Driver asíncrono para MongoDB |
| **PyMongo** | >=4.7.0 | Cliente MongoDB síncrono |
### Testing
| Librería | Versión | Propósito |
|----------|---------|-----------|
| **pytest** | >=8.2.0 | Framework de testing |
| **pytest-asyncio** | >=0.23.6 | Soporte para tests asíncronos |
| **httpx** | >=0.27.0 | Cliente HTTP para tests de API |
---
##  Arquitectura del Sistema
### Diagrama de Capas (Clean Architecture)
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│                    (API / Routes)                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  /api/v1/   │  │   /upload   │  │   exception_        │ │
│  │   users     │  │   (PDF)     │  │    handlers.py      │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└──────────────────────────┬──────────────────────────────────┘
                           │ Dependency Injection
┌──────────────────────────▼──────────────────────────────────┐
│                  APPLICATION LAYER                         │
│              (Services & DTOs)                               │
│  ┌─────────────────────┐  ┌───────────────────────────────┐   │
│  │   user_service.py   │  │      pdf_service.py          │   │
│  │   (Use Cases)       │  │   (Extracción & Checksum)    │   │
│  └─────────────────────┘  └───────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                  user_dto.py                            ││
│  │            (Data Transfer Objects)                       ││
│  └─────────────────────────────────────────────────────────┘│
└──────────────────────────┬──────────────────────────────────┘
                           │ Interfaces
┌──────────────────────────▼──────────────────────────────────┐
│                     DOMAIN LAYER                             │
│          (Entities & Repository Interfaces)                   │
│  ┌─────────────────────┐  ┌───────────────────────────────┐ │
│  │      user.py        │  │    user_repository.py          │ │
│  │   (Entidad Usuario) │  │   (Interface Repository)       │ │
│  └─────────────────────┘  └───────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────┘
                           │ Implementation
┌──────────────────────────▼──────────────────────────────────┐
│                  INFRASTRUCTURE LAYER                        │
│         (Database & External Services)                        │
│  ┌─────────────┐  ┌─────────────┐  ┌───────────────────────┐ │
│  │ connection. │  │ mongo_user_ │  │   schemas/            │ │
│  │     py      │  │repository.py│  │   user_schema.py     │ │
│  │ (MongoDB)   │  │(Implementation)│  │   (Validación)      │ │
│  └─────────────┘  └─────────────┘  └───────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
### Flujo de Datos (Procesamiento de PDF)
┌──────────┐     ┌──────────────┐     ┌──────────────────┐
│   PDF    │────▶│   API Layer  │────▶│ PDFService       │
│  Input   │     │  (Upload)    │     │ (Application)    │
└──────────┘     └──────────────┘     └────────┬─────────┘
                                                │
                       ┌────────────────────────┐
                       │  1. Validar formato    │
                       │  2. Generar checksum   │
                       │  3. Extraer texto      │
                       └────────┬───────────────┘
                                │
                       ┌────────▼────────┐
                       │ PyMuPDF (fitz)  │
                       │  extract_text() │
                       └────────┬────────┘
                                │
                       ┌────────▼────────┐
                       │  Response JSON  │
                       │  + Preview      │
                       └─────────────────┘
### CLI Standalone (Extracción Local)
┌──────────┐     ┌──────────────┐     ┌──────────────────┐
│   PDF    │────▶│   main.py    │────▶│ src/extractor.py │
│  File    │     │  (CLI Entry) │     │  (pypdf)         │
└──────────┘     └──────────────┘     └────────┬─────────┘
                                               │
                                  ┌────────────▼────────────┐
                                  │    src/processor.py     │
                                  │  - clean_text()         │
                                  │  - save_output()        │
                                  │  - get_estadisticas()   │
                                  └────────────┬────────────┘
                                               │
                                  ┌────────────▼────────────┐
                                  │     resultado.txt       │
                                  │   + Estadísticas        │
                                  └─────────────────────────┘
---
##  Principios de Ingeniería de Software
### 12-Factor App (Primeros 6 Principios)
| Principio | Implementación en el Proyecto |
|-----------|-------------------------------|
| **I. Codebase** | Un único repositorio Git con múltiples despliegues. Toda la aplicación versionada en un solo codebase. |
| **II. Dependencies** | Gestión mediante `pyproject.toml` y `uv`. Dependencias explícitas y aisladas. |
| **III. Config** | Configuración externalizada en archivo `.env` (DATABASE_URL, SECRET_KEY, DEBUG, etc.) |
| **IV. Backing Services** | MongoDB como servicio adjunto. URL de conexión configurable vía variables de entorno. |
| **V. Build, Release, Run** | Fase de Build: `uv pip install`. Release: Combinación build + config. Run: `uvicorn` |
| **VI. Processes** | Aplicación ejecutada como uno o más procesos sin estado. Cada proceso es independiente. |
### Principios SOLID
| Principio | Aplicación |
|-----------|------------|
| **S**ingle Responsibility | Cada capa tiene una responsabilidad única: API (presentación), Application (lógica), Domain (reglas de negocio), Infrastructure (datos) |
| **O**pen/Closed | Las interfaces de repositorio permiten extender sin modificar (ej: cambiar MongoDB por PostgreSQL) |
| **L**iskov Substitution | Las implementaciones de repositorio son intercambiables si cumplen la interfaz |
| **I**nterface Segregation | DTOs específicos para cada operación (UserDTO) |
| **D**ependency Inversion | La capa Application depende de abstracciones (interfaces), no de implementaciones concretas |
### Principios DRY, KISS y YAGNI
| Principio | Implementación |
|-----------|----------------|
| **DRY** (Don't Repeat Yourself) | Configuración centralizada en `app/core/config.py`, reutilización de servicios |
| **KISS** (Keep It Simple) | Extracción de PDF simple y directa sin over-engineering |
| **YAGNI** (You Ain't Gonna Need It) | Funcionalidades implementadas solo cuando son requeridas, sin features anticipadas |
---
##  Instalación y Configuración
### Requisitos Previos
- Python >= 3.12
- [UV](https://github.com/astral-sh/uv) - Gestor de paquetes ultra-rápido
- Docker & Docker Compose (para MongoDB)
- Git
### Paso 1: Clonar el Repositorio
```powershell
git clone <url-del-repositorio>
cd pdf-extactext
Paso 2: Configurar Variables de Entorno
# Crear archivo .env
copy .env.example .env
Editar .env con tus configuraciones:
# Configuración de la Base de Datos
DATABASE_URL=mongodb://localhost:27017
DB_NAME=pdf_extractor_db
# Seguridad y App
SECRET_KEY=desarrollo_secreto_utn_2026
DEBUG=True
API_V1_STR=/api/v1
Paso 3: Levantar MongoDB con Docker
# Iniciar el contenedor de MongoDB
docker-compose up -d
# Verificar que está corriendo
docker ps
Paso 4: Instalar Dependencias con UV
# Instalar UV si no lo tienes
# Windows (PowerShell):
irm https://astral.sh/uv/install.ps1 | iex
# Instalar dependencias del proyecto
uv pip install -e .
# O instalar desde pyproject.toml
uv pip install -r pyproject.toml --extra dev
Paso 5: Ejecutar la Aplicación
Modo CLI (Extracción Local):
python main.py "ruta/al/archivo.pdf" "ruta/salida.txt"
Modo API (Servidor Web):
# Development
uvicorn app.main:app --reload --port 8000
# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
Verificar que la API está corriendo:
curl http://localhost:8000/
---
 Uso de la Aplicación
CLI - Extracción Local
# Extracción básica
python main.py documento.pdf
# Con ruta de salida personalizada
python main.py documento.pdf resultados/mi_archivo.txt
# Salida esperada:
# ================================================================================
# PDF-EXTACTEXT - Extracción de Texto de PDF
# ================================================================================
#
#  PDF: documento.pdf
#  Salida: resultado.txt
#
# [1/4] Extrayendo texto...
#  ✓ 15432 caracteres extraídos
#
# [2/4] Limpiando texto...
#  ✓ 12345 caracteres limpios
#
# [3/4] Guardando resultado...
# ✓ Archivo guardado: C:\...\resultado.txt
#
# [4/4] Estadísticas:
#  • Caracteres: 12,345
#  • Palabras: 2,456
#  • Lineas: 234
#  • Parrafos: 45
#
# ✓ Completado
API REST - Endpoints
Método	Endpoint	Descripción
GET	/	Health check y estado del sistema
POST	/api/v1/upload	Subir PDF y extraer texto
GET	/api/v1/users	Listar usuarios
POST	/api/v1/users	Crear usuario
Ejemplo de uso con cURL:
# Subir un PDF
curl -X POST "http://localhost:8000/api/v1/upload" `
  -H "Content-Type: multipart/form-data" `
  -F "file=@mi_documento.pdf"
# Respuesta esperada:
# {
#   "filename": "mi_documento.pdf",
#   "checksum": "a1b2c3d4...",
#   "extracted_text_preview": "Primeros 100 caracteres del texto...",
#   "message": "Texto extraído correctamente"
# }
---
📁 Estructura del Proyecto
pdf-extactext/
├── 📄 README.md              # Este archivo
├── 📄 pyproject.toml          # Configuración del proyecto y dependencias
├── 📄 .env                   # Variables de entorno (no commitear)
├── 📄 .gitignore             # Archivos ignorados por Git
├── 📄 docker-compose.yml     # Configuración de MongoDB
│
├──  main.py                # Entry point CLI (orquestador)
│
├── 📁 app/                   # Aplicación principal (API)
│   ├── 📄 main.py            # Entry point FastAPI
│   │
│   ├── 📁 api/               # Layer: Presentation
│   │   ├── 📄 dependencies.py
│   │   ├── 📄 exception_handlers.py
│   │   └── 📁 v1/
│   │       ├── 📄 pdf_router.py      # Endpoints PDF
│   │       └── 📄 user_routes.py    # Endpoints Users
│   │
│   ├── 📁 application/       # Layer: Application
│   │   ├── 📁 dto/
│   │   │   └── 📄 user_dto.py
│   │   └── 📁 services/
│   │       ├── 📄 user_service.py
│   │       └── 📄 pdf_service.py    # Lógica de PDF
│   │
│   ├── 📁 core/              # Configuración central
│   │   ├── 📄 config.py      # Settings Pydantic
│   │   └── 📄 exceptions.py
│   │
│   ├── 📁 domain/            # Layer: Domain
│   │   ├── 📁 entities/
│   │   │   └── 📄 user.py
│   │   └── 📁 repositories/
│   │       └── 📄 user_repository.py  # Interface
│   │
│   ├── 📁 infrastructure/    # Layer: Infrastructure
│   │   ├── 📁 database/
│   │   │   ├── 📄 connection.py      # MongoDB connection
│   │   │   └── 📁 schemas/
│   │   │       └── 📄 user_schema.py
│   │   └── 📁 repositories/
│   │       └── 📄 mongo_user_repository.py  # Implementation
│   │
│   └── 📁 services/
│       └── 📄 pdf_service.py
│
├── 📁 src/                   # Scripts standalone (CLI)
│   ├── 📄 extractor.py       # Extracción con pypdf
│   └── 📄 processor.py        # Limpieza y procesamiento
│
├── 📁 tests/                 # Tests automatizados
│   ├── 📄 test_extractor.py
│   └── 📄 test_upload.py
│
└── 📄 conftest.py            # Configuración de pytest
---
🔌 API Endpoints
Health Check
GET /
Response:
{
  "message": "Bienvenida a la API de Extracción de PDF",
  "status": "Online",
  "db_name": "pdf_extractor_db"
}
Subir PDF
POST /api/v1/upload
Content-Type: multipart/form-data
file: <archivo.pdf>
Response 200:
{
  "filename": "documento.pdf",
  "checksum": "sha256_hash",
  "extracted_text_preview": "Primeros 100 caracteres...",
  "message": "Texto extraído correctamente"
}
Response 400 (Error):
{
  "detail": "Formato no válido"
}
---
Decisiones de Diseño
¿Por qué dos extractores de PDF?
Componente	Librería	Razón
src/extractor.py	pypdf	CLI simple, sin dependencias complejas, rápido de ejecutar
app/services/pdf_service.py	PyMuPDF	Permite lectura desde memoria (BytesIO) sin guardar archivos temporales
¿Por qué Clean Architecture?
1. Independencia de Frameworks: Podemos cambiar FastAPI por Flask sin tocar la lógica de negocio
2. Testabilidad: Las capas son fáciles de mockear y testear
3. Independencia de UI: Misma lógica sirve para CLI y API
4. Independencia de Base de Datos: Cambiar MongoDB por SQL requiere solo modificar Infrastructure
---
Testing
# Ejecutar todos los tests
uv run pytest
# Con cobertura
uv run pytest --cov=app --cov=src
# Tests específicos
uv run pytest tests/test_extractor.py
uv run pytest tests/test_upload.py
---
##  Licencia
Este proyecto es desarrollado con fines académicos para la cátedra de **Desarrollo de Software** de la **Universidad Tecnológica Nacional - Facultad Regional San Rafael (UTN FRSR)**.
**Integrantes:**
- Sirotiuk Juliana (10939)
- Jamardo Camila (10842)
- Ojeda Tomas (10882)
---
<div align="center">
⬆ Volver al inicio (#extracText---extractor-de-texto-pdf)
</div>
```



