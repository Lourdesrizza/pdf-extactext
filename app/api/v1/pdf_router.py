from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import PDFService

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # 1. Validación de formato
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")

    content = await file.read()
    
    # 2. Generar Checksum (Para el requerimiento de duplicados)
    checksum = PDFService.get_checksum(content)
    
    # 3. Extraer texto
    text = PDFService.extract_text(content)
    
    if not text:
        raise HTTPException(status_code=400, detail="El PDF no contiene texto extraíble")

    return {
        "filename": file.filename,
        "checksum": checksum,
        "extracted_text_preview": text[:100] + "...", # Un adelanto
        "message": "Texto extraído correctamente"
    }