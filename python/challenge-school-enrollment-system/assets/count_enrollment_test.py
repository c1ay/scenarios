import sys

sys.path.append("/home/labex/project")

import unittest
from count_enrollment import count_enrollment


class TestCountEnrollment(unittest.TestCase):
    def test_count_enrollment(self):
        enrollment_list1 = [
            1,
            2,
            3,
            4,
            4,
            5,
            5,
            5,
            6,
            6,
            7,
            8,
            8,
            8,
            9,
            9,
            10,
            10,
            11,
            12,
        ]
        enrollment_dict1 = {
            1: 1,
            2: 1,
            3: 1,
            4: 2,
            5: 3,
            6: 2,
            7: 1,
            8: 3,
            9: 2,
            10: 2,
            11: 1,
            12: 1,
        }
        self.assertEqual(count_enrollment(enrollment_list1), enrollment_dict1)

        enrollment_list2 = [
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            3,
            3,
            4,
            4,
            4,
            5,
            5,
            5,
            5,
            6,
            6,
            6,
            6,
            7,
            7,
            7,
            8,
            8,
            9,
            10,
            11,
            11,
            12,
            12,
        ]
        enrollment_dict2 = {
            1: 3,
            2: 2,
            3: 4,
            4: 3,
            5: 4,
            6: 4,
            7: 3,
            8: 2,
            9: 1,
            10: 1,
            11: 2,
            12: 2,
        }
        self.assertEqual(count_enrollment(enrollment_list2), enrollment_dict2)

        enrollment_list3 = []
        enrollment_dict3 = {i: 0 for i in range(1, 13)}
        self.assertEqual(count_enrollment(enrollment_list3), enrollment_dict3)

        enrollment_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        enrollment_dict4 = {i: 1 for i in range(1, 13)}
        self.assertEqual(count_enrollment(enrollment_list4), enrollment_dict4)

        enrollment_list5 = [1] * 100 + [2] * 200 + [3] * 300
        enrollment_dict5 = {
            1: 100,
            2: 200,
            3: 300,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
        }
        self.assertEqual(count_enrollment(enrollment_list5), enrollment_dict5)


if __name__ == "__main__":
    unittest.main()
