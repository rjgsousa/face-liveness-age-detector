import logging

import cv2
import numpy as np
from insightface.app import FaceAnalysis

from typing import Union


class FaceDetectionSpoofing:
    """Face Detection and Spoofing predictor

    """

    def __init__(self):
        # buffalo_l fails with children
        model_pack_name = 'buffalo_l'
        self.app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'], name=model_pack_name)
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.threshold = 0.75
        self.color_default = (0, 0, 255)  # deny by default

    def detect_face_and_spoof(self, img_or_img_path: Union[str, np.ndarray], preview_it=False) -> (bool, np.ndarray):
        """Detects and identifies faces in an image and determines if the face is spoofed.

        Args:
            img_or_img_path (str | np.ndarray):
                If a string, it represents the path to an image file.
                If a np.ndarray, it represents the image data as a NumPy array.
                Regardless the type, this method will handle the logic accordingly.
            preview_it (bool):
                preview the resulting frame or prioritize saving it to disk
        Returns:
            (success, img): (bool, np.ndarray)

        Example:
            >>> image = "/path/to/image.jpg"
            >>> fd = FaceDetectionSpoofing()
            >>> fd.detect_face_and_spoof(image)
        """

        if type(img_or_img_path) is str:
            img = cv2.imread(img_or_img_path)
        elif type(img_or_img_path) is np.ndarray:
            img = img_or_img_path
        else:
            logging.warning("wrong type")
            return False, np.zeros((0, 0))

        # the detection instruction
        try:
            faces = self.app.get(img)
        except:
            logging.warning("An exception occurred. continue processing")
            return False, np.zeros((0, 0))

        for face in faces:
            prob = 0
            color = self.color_default
            bbox = face.get('bbox', [])
            bbox = bbox.astype(np.int32)

            if len(bbox) == 4:
                prob = face.get('det_score', -1)

                # do we have confidence on the detection?
                if prob > self.threshold:
                    color = (255, 0, 0)

                cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, thickness=2)

            age = face.get('age', -1)
            gender = face.get('gender', -1)
            gender = 'women' if gender == 0 else 'man' if gender == 1 else 'unk'

            cv2.putText(img, f"Age: {age}", (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, color, 2)
            cv2.putText(img, f"Gender: {gender}", (bbox[0], bbox[1] + 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, color, 2)
            cv2.putText(img, f"Prob: {prob:.2f}", (bbox[0], bbox[1] + 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, color, 2)

        if preview_it:
            cv2.imshow('Face Detection', img)

        return True, img
