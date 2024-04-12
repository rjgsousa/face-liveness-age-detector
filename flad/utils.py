
import cv2
import numpy as np


def save_img(img: np.ndarray, file_path: str):
    """Saves image to a file

    Args:
        img:
        file_path:

    Returns:

    """
    cv2.imwrite(file_path, img)
