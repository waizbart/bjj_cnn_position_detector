import logging
from fastapi import APIRouter, Depends, File, Request, UploadFile, HTTPException

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/analyze/", summary="Analisar imagem para detecção de pose")
async def analyze_image(request: Request, file: UploadFile = File(...)):
    logger.info("Recebida imagem para análise.")

    pose_service = request.app.state.pose_service

    image_bytes = await file.read()
    result = pose_service.analyze_image(image_bytes)

    if "error" in result:
        logger.error(f"Erro na análise de pose: {result['error']}")
        raise HTTPException(status_code=400, detail=result["error"])

    return result
