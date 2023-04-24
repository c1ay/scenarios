import sys

sys.path.append("/home/labex/project")
from convert_color_space import convert_color_space

import unittest
import cv2
import numpy as np
from typing import Tuple


class TestColorSpaces(unittest.TestCase):
    def test_convert_color_space(self):
        # Test case for convert_color_space function
        image_path = "/tmp/img_test.jpg"
        original_image1, hsv_image = convert_color_space(image_path, "HSV")
        original_image2, lab_image = convert_color_space(image_path, "LAB")
        converted_image1 = cv2.cvtColor(original_image1, cv2.COLOR_BGR2HSV)
        converted_image2 = cv2.cvtColor(original_image2, cv2.COLOR_BGR2LAB)
        self.assertEqual((hsv_image != converted_image1).sum(), 0)
        self.assertEqual((lab_image != converted_image2).sum(), 0)


if __name__ == "__main__":
    unittest.main()
