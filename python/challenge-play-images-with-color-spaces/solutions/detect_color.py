import cv2
import numpy as np


def detect_color(
    image: np.ndarray, lower_bound: np.ndarray, upper_bound: np.ndarray
) -> np.ndarray:
    """
    Detect a specific color in the input image and create a mask highlighting the detected color.

    :param image: The input image.
    :param lower_bound: Lower bound of the target color in the HSV color space.
    :param upper_bound: Upper bound of the target color in the HSV color space.
    :return: The masked image with the target color highlighted.
    """
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Create a mask for the target color
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Apply the mask to the input image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image
