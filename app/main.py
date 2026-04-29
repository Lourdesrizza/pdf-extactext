from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.user_routes import router as user_router
from app.api.v1.pdf_router import router as pdf_router

app = FastAPI(
    title="PDF Extractor API", version=settings.API_V1_STR, debug=settings.DEBUG
)


@app.get("/")
def root():
    return {
        "message": "Bienvenida a la API de Extracción de PDF",
        "status": "Online",
        "db_name": settings.DB_NAME,
    }


# Routers de la API
app.include_router(user_router, prefix="/api/v1", tags=["users"])
app.include_router(pdf_router, prefix="/api/v1", tags=["Documentos"])
