import cv2
from typing import Tuple


def convert_color_space(image_path: str, color_space: str) -> Tuple:
    """
    Convert the input image to the specified color space.

    :param image_path: Path to the input image.
    :param color_space: The target color space ('RGB', 'HSV', or 'LAB').
    :return: A tuple containing the original image and the converted image.
    """
    # TODO: implement this function here.
    # Note: Do not change the existing code.


# # Example usage
# You can use the code below to save and see how your image looks in different color spaces during your code debugging.
# (Complete the above function to pass the challenge, the code below is not necessary for this challenge)
# image_path = 'images/img1.jpg'
# original_image, converted_hsv_image = convert_color_space(image_path, 'HSV')
# original_image, converted_lab_image = convert_color_space(image_path, 'LAB')
# # save the image
# cv2.imwrite("hsv_img01.jpg", converted_hsv_image)
# cv2.imwrite("lab_img01.jpg", converted_lab_image)
