import numpy as np
import cv2


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
    # TODO: implement this function here.
    # Note: Do not change the existing code.


# Example usage
# You can use the following code to save images during your debugging process, and view the effect of your code through the images.
# (Complete the above function to pass the challenge, the code below is not necessary for this challenge)

# image_path = 'images/img1.jpg'
# original_image = cv2.imread(image_path)
# blue_lower_bound = np.array([20, 20, 20])
# blue_upper_bound = np.array([230, 230, 230])
# blue_masked_image = detect_color(original_image, blue_lower_bound, blue_upper_bound)
# cv2.imwrite("blue_masked_image.jpg", blue_masked_image)
