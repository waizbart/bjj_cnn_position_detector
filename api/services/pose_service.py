import io
import logging
import base64

import numpy as np
from PIL import Image

from core.pose import KeypointDetector
from core.classifier import PoseClassifier

logger = logging.getLogger(__name__)

class PoseService:
    def __init__(self):
        self.detector = KeypointDetector()
        self.classifier = PoseClassifier()

    def analyze_image(self, image_bytes: bytes) -> dict:
        try:
            image = np.array(Image.open(io.BytesIO(image_bytes)), dtype=np.uint8)
            logger.info("Imagem carregada e convertida para array NumPy.")

            detection = self.detector.detect_keypoints(image)
            logger.info(f"Número de keypoints detectados: {len(detection)}")

            if len(detection) == 0:
                logger.warning("Nenhum keypoint detectado na imagem.")
                return {"error": "Nenhum keypoint detectado."}

            prediction = self.classifier.predict([detection])
            position_name = prediction[0] if prediction else "Desconhecida"
            logger.info(f"Pose prevista: {position_name}")

            img_with_keypoints = self.detector.draw_keypoints()
            logger.info("Keypoints desenhados na imagem.")

            img_pil = Image.fromarray(img_with_keypoints)
            img_buffer = io.BytesIO()
            img_pil.save(img_buffer, format="JPEG")
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            logger.info("Imagem codificada em base64.")

            return {
                "position_detected": position_name,
                "image_with_keypoints": img_base64,
                "image_format": "JPEG"
            }

        except Exception as e:
            logger.exception("Ocorreu um erro inesperado durante a análise da imagem.")
            return {"error": "Erro interno do servidor."}
