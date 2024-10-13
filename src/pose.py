import os
from PIL import Image
import cv2
import numpy as np
from models.vitpose.easy_ViTPose import VitInference
from huggingface_hub import hf_hub_download

class KeypointDetector:
    def __init__(self, model_size='h', yolo_size='x', dataset='coco'):
        self.model_size = model_size
        self.yolo_size = yolo_size
        self.dataset = 'coco'

        self.model_type = "torch"
        self.yolo_type = "torch"
        self.ext = '.pth'
        self.ext_yolo = '.pt'

        self.filename = f'{self.model_type}/{self.dataset}/vitpose-{self.model_size}-{self.dataset}{self.ext}'
        self.filename_yolo = f'yolov10{self.yolo_size}{self.ext_yolo}'
        self.yolo_path = os.path.join(os.path.dirname(__file__), 'models/vitpose', 'yolo_models', self.filename_yolo)

        print(f'Downloading model JunkyByte/easy_ViTPose/{self.filename}')
        model_path = hf_hub_download(
            repo_id='JunkyByte/easy_ViTPose', filename=self.filename)

        self.model = VitInference(model_path, self.yolo_path, self.model_size,
                                  dataset=self.dataset, yolo_size=640,
                                  yolo_confidence_threshold=0.2, is_video=False)

    def detect_keypoints(self, img):
        frame_keypoints = self.model.inference(img)

        return frame_keypoints

    def draw_keypoints(self, confidence_threshold=0.2, show_yolo=False):
        img_with_keypoints = self.model.draw(
            show_yolo=show_yolo, confidence_threshold=confidence_threshold)
        return img_with_keypoints

    def display_image(self, img_with_keypoints, wait=False):
        cv2.imshow("Inference Image", img_with_keypoints[..., ::-1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    detector = KeypointDetector()

    image_path = os.path.join(os.path.dirname(__file__), '..', 'assets/images', 'take01.jpeg')
    image = np.array(Image.open(image_path), dtype=np.uint8)

    keypoints = detector.detect_keypoints(image)
    print(f'Número de keypoints detectados: {len(keypoints)}')

    img_with_keypoints = detector.draw_keypoints()

    detector.display_image(img_with_keypoints, wait=True)


if __name__ == "__main__":
    main()
