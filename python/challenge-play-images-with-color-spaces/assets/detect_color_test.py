import sys

sys.path.append("/home/labex/project")


import unittest
import cv2
import numpy as np
from typing import Tuple
from detect_color import detect_color


class TestColorSpaces(unittest.TestCase):
    def test_detect_color(self):
        # Test case for detect_color function
        image_path = "/tmp/img_test.jpg"
        image = cv2.imread(image_path)
        lower_bound = np.array([100, 150, 50])
        upper_bound = np.array([140, 255, 255])

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        masked_image1 = cv2.bitwise_and(image, image, mask=mask)
        masked_image2 = detect_color(image, lower_bound, upper_bound)

        self.assertEqual((masked_image1 != masked_image2).sum(), 0)


if __name__ == "__main__":
    unittest.main()
