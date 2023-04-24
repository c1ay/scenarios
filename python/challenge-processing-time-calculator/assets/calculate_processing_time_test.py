import sys

sys.path.append("/home/labex/project")

import unittest
from calculate_processing_time import calculate_processing_time


class TestCalculateProcessingTime(unittest.TestCase):
    def test_calculate_processing_time(self):
        num_pages = 25
        expected_output = 3
        self.assertEqual(calculate_processing_time(num_pages), expected_output)

        num_pages = 150
        expected_output = 7
        self.assertEqual(calculate_processing_time(num_pages), expected_output)

        num_pages = 10
        expected_output = 1
        self.assertEqual(calculate_processing_time(num_pages), expected_output)

        num_pages = 50
        expected_output = 3
        self.assertEqual(calculate_processing_time(num_pages), expected_output)


if __name__ == "__main__":
    unittest.main()
