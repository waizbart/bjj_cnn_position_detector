from utils.constants import LABELS_VALUES
import numpy as np
import tensorflow as tf

class PoseClassifier:
    def __init__(self):
        self.model = tf.keras.models.load_model("./models/pose_classifier/v5.keras")

    def predict(self, detections):
        if len(detections) == 0:
            raise ValueError("Nenhuma detecção de pose")
        
        detections_keypoints = []

        for detection in detections:
            keypoints = np.array([detection[0][:, :2][:, ::-1]])

            if len(detection) > 1:
                keypoints2 = np.array([detection[1][:, :2][:, ::-1]])
            else:
                keypoints2 = np.array([[[0, 0]] * 17])

            keypoints = np.concatenate((keypoints, keypoints2), axis=0)
            keypoints = keypoints.reshape(1, 17 * 2 * 2)
            max_x = np.max(keypoints)
            normalized_keypoints = keypoints / max_x
            
            detections_keypoints.append(normalized_keypoints)
            
        keypoints = np.concatenate(detections_keypoints, axis=0)
        keypoints = keypoints.reshape(-1, 17 * 2 * 2) 

        predictions = self.model.predict(keypoints)
        
        return [LABELS_VALUES[np.argmax(prediction)] for prediction in predictions]
