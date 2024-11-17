import base64
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()
logger = logging.getLogger(__name__)

@router.websocket("/ws/analyze/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("Conexão WebSocket aceita.")

    pose_service = websocket.app.state.pose_service

    try:
        while True:
            data = await websocket.receive_text()
            logger.info("Dados recebidos do cliente.")

            try:
                image_bytes = base64.b64decode(data)
            except Exception as e:
                logger.error("Falha ao decodificar dados da imagem.")
                await websocket.send_json({"error": "Dados de imagem inválidos."})
                continue

            result = pose_service.analyze_image(image_bytes)

            if "error" in result:
                logger.error(f"Erro na análise de pose: {result['error']}")
                await websocket.send_json({"error": result["error"]})
                continue

            await websocket.send_json(result)

    except WebSocketDisconnect:
        logger.info("Conexão WebSocket encerrada pelo cliente.")
    except Exception as e:
        logger.exception("Ocorreu um erro inesperado no endpoint WebSocket.")
        await websocket.close(code=1011, reason="Erro interno do servidor")
