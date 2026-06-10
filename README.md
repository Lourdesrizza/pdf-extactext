> Extractor de texto de archivos PDF con persistencia en MongoDB.

![status](https://img.shields.io/badge/status-active-brightgreen)
![python](https://img.shields.io/badge/python-3.12-blue)
![fastapi](https://img.shields.io/badge/fastapi-0.136.0-009688)
![license](https://img.shields.io/badge/license-MIT-green)
![tdd](https://img.shields.io/badge/metodología-TDD-orange)
![uv](https://img.shields.io/badge/gestor-uv-purple)

---

## Descripción

Esta aplicación permite a los usuarios:

- **Subir archivos PDF** — Los envía el cliente en formato binario.
- **Extraer texto automáticamente** — Lee el contenido directamente en memoria, sin guardar archivos temporales.
- **Persistir en MongoDB** — Guarda el documento con su checksum SHA-256 para detectar duplicados.
- **Gestionar documentos** — CRUD completo: obtener, listar, actualizar y eliminar documentos.

Está construida siguiendo arquitectura empresarial en capas, **TDD** (Test-Driven Development), y los principios **YAGNI, DRY, KISS, SOLID**, como lo exigen los criterios de evaluación del Proyecto 2026 de Desarrollo de Software — UTN FRSR.

---

## Integrantes

| Nombre | Legajo |
|---|---|
| Magallanes Angelina | 10853 |
| Puente Maité | 10902 |
| Rizza Lourdes | 10913 |
| Roda Jeremías | 10917 |

---

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python | Lenguaje principal |
| Control de versiones | Git & GitHub |
| Entorno de Desarrollo | Visual Studio Code |
| FastAPI + Uvicorn | Framework web y servidor ASGI |
| pypdf / PyMuPDF | Extracción de texto de PDFs |
| Motor (async MongoDB) | Persistencia de documentos |
| pytest + pytest-asyncio | Testing con cobertura |
| uv | Gestión de dependencias |
| Docker | Contenedor de MongoDB |

---

## Estructura del Proyecto

```text
extracText/
├── app/
│   ├── api/               # Routers de FastAPI (Capa de presentación)
│   ├── application/       # Casos de Uso (orquestación)
│   ├── domain/            # Entidades y excepciones (reglas de negocio)
│   ├── infrastructure/    # MongoDB, servicios concretos
│   ├── services/          # PDFService (lógica de extracción)
│   ├── static/            # CSS personalizado para Swagger UI
│   └── main.py            # Punto de entrada de la aplicación
├── src/                   # Módulos auxiliares (extractor / processor)
├── tests/
│   ├── domain/            # Tests de dominio y servicios
│   ├── presentation/      # Tests de endpoints HTTP
│   └── data/              # Tests de repositorio y MongoDB
├── docs/                  # Diagramas UML y guía de estudio
├── .env.example           # Variables de entorno de ejemplo
├── pyproject.toml         # Dependencias y configuración
├── docker-compose.yml     # Contenedor de MongoDB
└── README.md
```

---

## Arquitectura

El proyecto aplica **Arquitectura de Aplicaciones Empresariales** en cuatro capas:

```
┌──────────────────────────────────────────┐
│   1. API / Presentación  (FastAPI Routers) │  ← Recibe y responde requests HTTP
├──────────────────────────────────────────┤
│   2. Aplicación  (Services / Use Cases)   │  ← Orquesta lógica de negocio
├──────────────────────────────────────────┤
│   3. Dominio  (Entidades / Excepciones)   │  ← Reglas de negocio puras
├──────────────────────────────────────────┤
│   4. Infraestructura  (MongoDB / Motor)   │  ← Implementaciones concretas
└──────────────────────────────────────────┘
```

**Flujo de una petición de subida de PDF:**

```
Cliente envía POST /api/v1/upload
  → pdf_router.py  (valida extensión .pdf)
  → PDFService.validate_pdf_content()  (tamaño, firma %PDF)
  → PDFService.get_checksum()  (SHA-256)
  → PDFService.extract_text()  (PyMuPDF)
  → Respuesta JSON con preview del texto
```

---

## Requisitos del Proyecto (Etapa N° 1)

Según la consigna oficial de UTN FRSR 2026:

| Requisito | Cumplimiento |
|---|---|
| Enviar y procesar archivo PDF | ✅ `POST /api/v1/upload` |
| Extraer solo texto del contenido | ✅ `PDFService.extract_text()` |
| Persistir con checksum SHA-256 | ✅ `MongoDocumentRepository` |
| CRUD de documentos persistidos | ✅ Endpoints GET / PATCH / DELETE |
| Validar formato y tamaño del PDF | ✅ Firma `%PDF`, límite 5 MB |
| No persistir temporalmente | ✅ Procesamiento en memoria |
| No duplicar documentos en BD | ✅ Búsqueda por checksum previa |
| Lenguaje: Python | ✅ Python 3.12 |
| Framework: FastAPI | ✅ FastAPI 0.136 |
| Gestor de paquetes: uv | ✅ `uv sync` |
| Metodología: TDD | ✅ `tests/` con pytest |
| Gestión: GitHub Projects | ✅ |

---

## Endpoints principales

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/api/v1/upload` | Sube y procesa un PDF |
| `GET` | `/api/v1/documents` | Lista todos los documentos |
| `GET` | `/api/v1/documents/{id}` | Busca documento por ID |
| `GET` | `/api/v1/documents/checksum/{hash}` | Busca por checksum SHA-256 |
| `PATCH` | `/api/v1/documents/{id}` | Actualiza el nombre del archivo |
| `DELETE` | `/api/v1/documents/{id}` | Elimina un documento |
| `POST` | `/api/v1/users/` | Crea un usuario |
| `GET` | `/api/v1/users/{id}` | Obtiene usuario por ID |

La documentación interactiva (Swagger UI) está disponible en:

```
http://127.0.0.1:8000/docs
```

---

## Guía de Instalación

### Requisitos previos

- Python 3.12 o superior
- Docker Desktop
- Git

### Paso 1 — Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/extracText.git
cd extracText
```

### Paso 2 — Instalar uv

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy BypassCurrent -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Paso 3 — Instalar dependencias

```bash
uv sync --all-extras
```

### Paso 4 — Configurar variables de entorno

```bash
cp .env.example .env
```

Editar `.env` con los valores correspondientes:

```env
API_V1_STR=/api/v1
DEBUG=True
DATABASE_URL=mongodb://localhost:27017
DB_NAME=pdf_extractor_db
SECRET_KEY=cambiar_esta_clave_en_cada_entorno
```

### Paso 5 — Levantar MongoDB con Docker

```bash
docker run -d -p 27017:27017 --name mongo mongo:7
```

O usando el `docker-compose.yml` incluido:

```bash
docker-compose up -d basededatos
```

### Paso 6 — Levantar el servidor

```bash
uv run uvicorn app.main:app --reload
```

---

## Ejecución de Tests

```bash
# Todos los tests
uv run pytest

# Solo tests unitarios (sin MongoDB)
uv run pytest tests/domain tests/presentation

# Tests de integración con MongoDB real (requiere Docker activo)
uv run pytest tests/data/test_mongo_real.py

# Con detalle de cada test
uv run pytest -v
```

> ⚠️ Los tests en `tests/data/test_mongo_real.py` requieren que MongoDB esté corriendo en `localhost:27017`.

---

## Principios aplicados

### 12-Factor App

| Factor | Aplicación |
|---|---|
| Codebase | Un único repositorio versionado en GitHub |
| Dependencias | Declaradas en `pyproject.toml`, gestionadas con `uv` |
| Configuraciones | Variables de entorno via `.env` y `pydantic-settings` |
| Backing Services | MongoDB tratado como recurso externo (Docker) |
| Procesos | Stateless — sin estado persistente en memoria entre requests |
| Puerto | Expuesto explícitamente en `8000` via Uvicorn |

### Código Limpio

- **DRY** — Lógica de validación y extracción centralizada en `PDFService`.
- **KISS** — Cada módulo tiene una única responsabilidad clara.
- **YAGNI** — Solo se implementa lo requerido por la consigna.
- **SOLID** — Repositorios abstraídos con interfaces (`DocumentRepository`, `UserRepository`), inyección de dependencias via FastAPI `Depends`.

---

## Licencia

MIT License — Copyright (c) 2026 UTN FRSR — Desarrollo de Software

---

*UTN — Facultad Regional San Rafael — 3° Año — Ingeniería en Sistemas de Información — 2026*
