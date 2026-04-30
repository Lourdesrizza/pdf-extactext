extracText - Extractor de texto PDF
Proyecto académico - Desarrollo de Software (3er Año) - UTN FRSR - 2026.

Descripción del Proyecto
extracText es una aplicación de extracción de texto de archivos PDF desarrollada siguiendo principios de arquitectura limpia. El sistema permite extraer texto de forma local (CLI) o mediante una API RESTful, almacenando metadatos y resultados en MongoDB y detectando archivos duplicados mediante checksum SHA256.

Integrantes del Equipo

Legajo 10853 - Magallanes Angelina
Legajo 10902 - Puente Maite
Legajo 10913 - Rizza Lourdes
Legajo 10917 - Roda Jeremias



Tecnologías y Librerías

Core: Python 3.12+, FastAPI, Pydantic

Base de Datos: MongoDB (Motor asíncrono)

Gestión: UV (Gestor de paquetes), Docker

Procesamiento PDF: pypdf para CLI y PyMuPDF para API

Arquitectura del Sistema

El proyecto se organiza en 4 capas desacopladas siguiendo Clean Architecture:

Presentación: API Routers y entrada de CLI

Aplicación: Servicios de lógica y DTOs

Dominio: Entidades y reglas de negocio puras

Infraestructura: Implementación de base de datos y librerías externas

Instalación y Configuración

Paso 1: Clonar el Repositorio
git clone https://github.com/TU_USUARIO/extracText.git
cd extracText

Paso 2: Configurar Entorno
Copia el archivo .env.example a .env y ajusta las variables de entorno necesarias.

Paso 3: Instalar Dependencias
uv sync --all-extras

Paso 4: Levantar Infraestructura
docker run -d -p 27017:27017 --name mongo mongo:7

Uso de la Aplicación

Modo API: uv run uvicorn app.main:app --reload

Modo CLI: python main.py "ruta/al/archivo.pdf"

Licencia

Este proyecto es desarrollado con fines académicos para la carrera de Ingeniería en Sistemas de Información de la Universidad Tecnológica Nacional - Facultad Regional San Rafael (UTN FRSR).

UTN FRSR - 2026