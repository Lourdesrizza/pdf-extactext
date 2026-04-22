from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="PDF Extractor API",
    version=settings.API_V1_STR,
    debug=settings.DEBUG
)

@app.get("/")
def root():
    return {
        "message": "Bienvenida a la API de Extracción de PDF",
        "status": "Online",
        "db_name": settings.DB_NAME
    }
    
# Al principio de los imports:
from app.api.v1.pdf_router import router as pdf_router

# Debajo de app = FastAPI(...):
app.include_router(pdf_router, prefix="/api/v1", tags=["Documentos"])