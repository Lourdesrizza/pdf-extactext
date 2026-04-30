```markdown
# extracText - Extractor de Texto PDF[cite: 1]

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-4.7+-47A248.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)

**Proyecto Académico - Desarrollo de Software (3er Año)**[cite: 1]
**UTN FRSR - 2026**[cite: 1]

</div>

---

## 📝 Descripción del Proyecto[cite: 1]
**extracText** es una herramienta eficiente desarrollada en Python para la extracción y procesamiento de texto desde archivos PDF[cite: 1]. El sistema permite:
* **Subir archivos PDF**: Los envía el cliente en formato binario[cite: 1].
* **Extraer texto automáticamente**: Lee el contenido directamente en memoria, sin guardar archivos temporales[cite: 1].
* **Persistir en MongoDB**: Almacena el documento con su checksum (SHA-256) para evitar duplicados[cite: 1].
* **Gestionar documentos**: CRUD completo para obtener, listar, actualizar y eliminar documentos[cite: 1].

Está construida siguiendo arquitectura empresarial en capas, TDD (Test-Driven Development), y principios YAGNI, DRY, KISS y SOLID[cite: 1].

---

## 👥 Integrantes del Equipo[cite: 1]
| Legajo | Nombre | Rol Principal |
|--------|--------|---------------|
| **10939** | Sirotiuk Juliana | Domain Layer & Entities[cite: 1] |
| **10842** | Jamardo Camila | Application Layer & Services[cite: 1] |
| **10882** | Ojeda Tomas | Infrastructure & API Layer[cite: 1] |

**Cátedra:** Desarrollo de Software (3er Año - UTN FRSR - 2026)[cite: 1]

---

## 🛠 Tecnologías y Herramientas[cite: 1]
* **Lenguaje:** Python 3.12+[cite: 1]
* **Framework Web:** FastAPI 0.115.0+[cite: 1]
* **Servidor ASGI:** Uvicorn[cite: 1]
* **Base de Datos:** MongoDB (Driver Motor para async)[cite: 1]
* **Control de Versiones:** Git & GitHub[cite: 1]
* **IDE:** Visual Studio Code[cite: 1]

### Librerías para el procesamiento de PDFs[cite: 1]
* **Si el PDF tiene texto seleccionable**:[cite: 1]
    * **pdfplumber**: Obtiene texto estructurado y detecta tablas/columnas[cite: 1].
    * **PyMuPDF (fitz)**: Extrae textos e imágenes y renderiza páginas[cite: 1].
    * **pypdf**: Gestiona metadatos, une, divide y rota páginas[cite: 1].
* **Si el PDF está escaneado (imágenes)**:[cite: 1]
    * **pytesseract + pdf2image**: Aplica técnicas OCR para extraer texto de imágenes[cite: 1].
* **Si se necesita extraer tablas**:[cite: 1]
    * **Camelot**: Detecta tablas definidas y exporta a CSV o DataFrame[cite: 1].

---

## 🏗 Arquitectura del Sistema[cite: 1]
El proyecto sigue una arquitectura en **4 capas bien separadas**[cite: 1]:
```text
┌─────────────────────────────────────────┐
│  API (FastAPI Routers)                  │  ← Capa de presentación
├─────────────────────────────────────────┤
│  Application (Use Cases)                │  ← Orquestación de lógica
├─────────────────────────────────────────┤
│  Domain (Entidades, Excepciones)        │  ← Reglas de negocio puro
├─────────────────────────────────────────┤
│  Infrastructure (MongoDB, Services)     │  ← Implementaciones concretas
└─────────────────────────────────────────┘
```

Cada capa tiene responsabilidades claras y se comunica a través de interfaces abstractas[cite: 1].

---

## ⚙️ Principios de Ingeniería Aplicados[cite: 1]

### Requisitos 12-Factor App[cite: 1]
* **Codebase**: Única base de código versionada en un repositorio[cite: 1].
* **Dependencias**: Declaradas explícitamente mediante `pyproject.toml`[cite: 1].
* **Variables de Entorno**: Configuración de aspectos sensibles del entorno[cite: 1].
* **Configuraciones**: Mantenidas separadas del código para distintos entornos[cite: 1].
* **Backing Services**: Servicios externos tratados como recursos intercambiables[cite: 1].
* **Procesos**: Ejecución como procesos sin estados persistentes en memoria[cite: 1].
* **Asignación de Puertos**: Exportación de servicios mediante puertos definidos[cite: 1].

### Código Limpio (SOLID & DRY)[cite: 1]
* **DRY**: Don't Repeat Yourself (evitar duplicación de lógica)[cite: 1].
* **KISS**: Keep It Simple, Stupid (mantener simplicidad)[cite: 1].
* **YAGNI**: You Aren't Gonna Need It (programar solo lo necesario)[cite: 1].
* **SOLID**:[cite: 1]
    * **S**: Responsabilidad única (una clase, una tarea)[cite: 1].
    * **O**: Abierto/Cerrado (ampliable pero no modificable)[cite: 1].
    * **L**: Sustitución de Liskov (clases hijas intercambiables)[cite: 1].
    * **I**: Segregación de interfaces (interfaces pequeñas y específicas)[cite: 1].
    * **D**: Inversión de dependencias (depender de abstracciones)[cite: 1].

---

## 🚀 Guía de Instalación[cite: 1]

### Requisitos previos[cite: 1]
Asegúrese de tener instalado:[cite: 1]
* **Python 3.12+**[cite: 1]
* **Docker Desktop**[cite: 1]
* **Git**[cite: 1]

### Paso 1: Clonar el repositorio[cite: 1]
```bash
git clone [https://github.com/TU_USUARIO/extracText.git](https://github.com/TU_USUARIO/extracText.git)
cd extracText
```

### Paso 2: Instalar gestor de paquetes `uv`[cite: 1]
**Windows (PowerShell)**:[cite: 1]
```powershell
powershell -ExecutionPolicy BypassCurrent -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```
**macOS/Linux**:[cite: 1]
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```

### Paso 3: Instalación de dependencias y configuración[cite: 1]
```bash
# Instalar dependencias
uv sync --all-extras

# Configurar variables de entorno
cp .env.example .env
```

### Paso 4: Levantar MongoDB con Docker[cite: 1]
```bash
# Iniciar contenedor
docker run -d -p 27017:27017 --name mongo mongo:7

# Verificar estado
docker ps
```

---

## 💻 Ejecución y Uso[cite: 1]

### Iniciar el servidor[cite: 1]
```bash
uv run uvicorn app.main:app --reload
```
Verá el mensaje: `Uvicorn running on http://127.0.0.1:8000`[cite: 1].

### Interfaz Interactiva (Swagger)[cite: 1]
Acceda a: `http://127.0.0.1:8000/docs` para probar todos los endpoints[cite: 1].

---

## 📁 Estructura del Proyecto[cite: 1]
```text
pdf-extactext/
├── app/                # Aplicación principal (API)
│   ├── api/            # Layer: Presentation (Routers)
│   ├── application/    # Layer: Application (Use Cases/Services)
│   ├── domain/         # Layer: Domain (Entities)
│   └── infrastructure/ # Layer: Infrastructure (MongoDB/Services)
├── src/                # Scripts standalone (CLI)
├── tests/              # Tests automatizados
└── pyproject.toml      # Configuración y dependencias
```

---

<div align="center">
UTN - Facultad Regional San Rafael - Tercer año - Desarrollo de Software - Ingeniería en Sistemas de Información - 2026[cite: 1]
</div>
```