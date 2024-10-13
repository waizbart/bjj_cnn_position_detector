import os
from utils.constants import LABELS_VALUES
import cv2
import numpy as np
import tensorflow as tf

class PoseClassifier:
    def __init__(self):
        self.model = tf.keras.models.load_model("./models/pose_classifier/v1.h5")

    def predict(self, detection_keypoints):
        if len(detection_keypoints) == 0:
            raise ValueError("Nenhuma detecção de pose")

        keypoints = np.array([detection_keypoints[0][:, :2][:, ::-1]])

        if len(detection_keypoints) > 1:
            keypoints2 = np.array([detection_keypoints[1][:, :2][:, ::-1]])
        else:
            keypoints2 = np.array([[[0, 0]] * 17])

        keypoints = np.concatenate((keypoints, keypoints2), axis=0)
        keypoints = keypoints.reshape(1, 17 * 2 * 2)
        max_x = np.max(keypoints)
        normalized_keypoints = keypoints / max_x

        prediction = self.model.predict(normalized_keypoints)
        
        return LABELS_VALUES[np.argmax(prediction)]
