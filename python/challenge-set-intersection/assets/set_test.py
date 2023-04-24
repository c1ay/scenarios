import unittest
import sys

sys.path.append("/home/labex/project/")
from set import *


class TestSetIntersection(unittest.TestCase):
    def test_set_intersection(self):
        self.assertEqual(set_intersection({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}), {4, 5})
        self.assertEqual(set_intersection({1, 2, 3}, {4, 5}), set())
        self.assertEqual(set_intersection(set(), set()), set())


if __name__ == "__main__":
    unittest.main()
