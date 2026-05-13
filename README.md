# extracText - Extractor de Texto PDF

Proyecto desarrollado para la asignatura **Desarrollo de Software** (3er Año - UTN - FRSR). El objetivo es crear una herramienta eficiente en Python para la extracción y procesamiento de texto desde archivos PDF.

**Integrantes**
* **Magallanes Angelina 10853**
* **Puente Maite 10902**
* **Rizza Lourdes 10913**
* **Roda Jeremias 10917**

**Características**
* Extracción de texto plano de archivos PDF.
* Interfaz de línea de comandos (CLI).
* Gestión de dependencias mediante entornos virtuales.
* Arquitectura orientada a la mantenibilidad y código limpio.

**Tecnologías y Herramientas**
* **Lenguaje**: Python
* **Librerías**: Pypdf (fitz)
* **Control de Versiones**: Git y GitHub
* **Entorno de Desarrollo**: Visual Studio Code

**Librerías para el procesamiento de PDFs**
* **Si el PDF tiene texto seleccionable (pdfplumber, PyMuPDF, pypdf)**:
    * **pdfplumber**: Permite obtener texto de forma estructurada y detectar elementos como tablas y columnas.
    * **PyMuPDF**: Permite extraer textos e imágenes, renderizar páginas y realizar modificaciones sobre archivos.
    * **pypdf**: Permite unir, dividir y rotar páginas, además de gestionar metadatos.
* **Si el PDF está escaneado con imágenes (pytesseract + pdf2image)**:
    * Estos componentes juntos permiten procesar archivos PDF escaneados; pdf2image convierte cada página en una imagen y pytesseract aplica técnicas de reconocimiento óptico de caracteres (OCR) para extraer el texto.
* **Si se necesita extraer tablas (pdfplumber, Camelot)**:
    * **Camelot**: Permite detectar tablas precisamente cuando están bien definidas en el documento y permite exportar los datos a formatos como CSV o DataFrame.

 **Principios de Ingeniería Aplicados**

**Requisitos 12-Factor App**
* **Codebase**: Se debe contar con una única base de código versionada en un repositorio.
* **Dependencias**: Todas las dependencias deben declararse explícitamente mediante pyproject.toml para evitar errores en el trabajo en equipo.
* **Variables de Entorno**: Utilizadas para configurar aspectos sensibles o particulares del entorno de ejecución.
* **Configuraciones**: Las configuraciones del sistema deben mantenerse separadas del código para ejecutarse en distintos entornos sin modificaciones.
* **Backing Services**: Servicios externos como bases de datos, colas de mensajes o storage deben tratarse como recursos intercambiables.
* **Construir, Desplegar, Ejecutar**: El proceso incluye preparar el proyecto, combinar el build con la configuración y finalmente ejecutar.
* **Procesos**: Se debe ejecutar como uno o más procesos sin estados persistentes en memoria interna.
* **Asignación de Puertos**: La aplicación debe exponer servicios a través de puertos definidos.

**Código Limpio**
* **DRY (Don't Repeat Yourself)**: Evitar la duplicación de código y lógica innecesaria.
* **KISS (Keep It Simple, Stupid)**: Mantener el código simple y claro sin complejidades innecesarias.
* **YAGNI (You Aren't Gonna Need It)**: Programar únicamente lo que es necesario.
* **SOLID**: Sistema que busca que el código sea como piezas independientes que encajan perfectamente para ser intercambiables.
* **S (Responsabilidad única)**: Una clase debe hacer una sola cosa.
* **O (Abierto/Cerrado)**: El código se debe poder ampliar, pero no modificar.
* **L (Sustitución de Liskov)**: Una clase hija debe poder usarse en lugar de su padre sin romper el sistema.
* **I (Segregación de interfaces)**: Es mejor tener muchas interfaces pequeñas que una gigante con métodos sin uso.
* **D (Inversión de Dependencias)**: No se depende de clases concretas, sino de abstracciones e interfaces.

**Descripción de la Aplicación**
* **Subir archivos PDF**: Los envía el cliente en formato binario.
* **Extraer texto automáticamente**: Lee el contenido directamente en memoria sin guardar archivos temporales.
* **Persistir en MongoDB**: Guarda el documento con su checksum SHA-256 para detectar duplicados.
* **Gestionar documentos**: Ofrece un CRUD completo para obtener, listar, actualizar y eliminar documentos.

**Arquitectura del Sistema**

┌─────────────────────────────────────────┐
│  API (FastAPI Routers)                  │  ← Capa de presentación
├─────────────────────────────────────────┤
│  Application (Use Cases)                │  ← Orquestación de lógica
├─────────────────────────────────────────┤
│  Domain (Entidades, Excepciones)        │  ← Reglas de negocio puro
├─────────────────────────────────────────┤
│  Infrastructure (MongoDB, Services)     │  ← Implementaciones concretas
└─────────────────────────────────────────┘

**Guía de Instalación**
* **Software requerido**: Python 3.12 o superior, Docker Desktop y Git.
* **Paso 1 - Clonar el repositorio**: git clone [https://github.com/TU_USUARIO/extracText.git](https://github.com/TU_USUARIO/extracText.git)
* **Paso 2 - Instalar uv en Windows (PowerShell)**: powershell -ExecutionPolicy BypassCurrent -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
* **Paso 3 - Instalar uv en macOS o Linux**: curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
* **Paso 4 - Instalar dependencias**: uv sync --all-extras
* **Paso 5 - Configurar variables de entorno**: cp .env.example .env
* **Paso 6 - Levantar MongoDB con Docker**: docker run -d -p 27017:27017 --name mongo mongo:7

**Ejecución de la Aplicación**
* **Levantar el servidor**: uv run uvicorn app.main:app --reload
* **Acceder a la interfaz web**: Abrir el navegador en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para ver el Swagger UI interactivo.

UTN - Facultad Regional San Rafael - Tercer año - Desarrollo de Software - Ingeniería en Sistemas de Información - 2026