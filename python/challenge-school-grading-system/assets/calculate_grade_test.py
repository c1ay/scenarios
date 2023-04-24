import sys

sys.path.append("/home/labex/project")

import unittest
from calculate_grade import calculate_grade


class TestCalculateGrade(unittest.TestCase):
    def test_calculate_grade(self):
        student_info1 = {
            "name": "John Smith",
            "assignments": [90, 85, 75, 100],
            "tests": [80, 85],
            "attendance": 90,
        }
        self.assertEqual(calculate_grade(student_info1), 93)

        student_info2 = {
            "name": "Jane Doe",
            "assignments": [80, 75, 70, 85],
            "tests": [90, 95],
            "attendance": 95,
        }
        self.assertEqual(calculate_grade(student_info2), 90)


if __name__ == "__main__":
    unittest.main()
