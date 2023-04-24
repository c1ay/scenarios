import cv2
from typing import Tuple


def convert_color_space(image_path: str, color_space: str) -> Tuple:
    """
    Convert the input image to the specified color space.

    :param image_path: Path to the input image.
    :param color_space: The target color space ('RGB', 'HSV', or 'LAB').
    :return: A tuple containing the original image and the converted image.
    """
    # Read the input image
    image = cv2.imread(image_path)
    # Convert the image to the specified color space
    if color_space == "RGB":
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif color_space == "HSV":
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    elif color_space == "LAB":
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    else:
        raise ValueError("Invalid color space")

    return image, converted_image
