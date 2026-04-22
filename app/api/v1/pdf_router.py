from fastapi import APIRouter, UploadFile, File, HTTPException
import io

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # 1. VALIDACIÓN DE FORMATO (Requerimiento de la Etapa 1)
    # Verificamos la extensión y el tipo de contenido
    if not file.filename.endswith(".pdf") and file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400, 
            detail="El archivo debe ser un PDF"
        )

    # 2. VALIDACIÓN DE TAMAÑO (Consideraciones)
    # Leemos el contenido para saber cuánto pesa (ejemplo: max 5MB)
    content = await file.read()
    max_size = 5 * 1024 * 1024  # 5 Megabytes
    
    if len(content) > max_size:
        raise HTTPException(
            status_code=400, 
            detail="El archivo es demasiado grande (máximo 5MB)"
        )

    # 3. PROCESAMIENTO (Aquí llamaremos al Rol de Servicio más adelante)
    # Por ahora devolvemos un éxito para que el test pase
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "message": "Archivo recibido y validado con éxito"
    }