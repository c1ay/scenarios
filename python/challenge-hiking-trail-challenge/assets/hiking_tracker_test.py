import sys

sys.path.append("/home/labex/project")

import unittest
from hiking_tracker import hiking_tracker


class TestHikingTrail(unittest.TestCase):
    def test_hiking_tracker(self):
        hikers = [("John", 3), ("Jane", 5), ("Bob", 8)]
        expected_output = {"John": 3, "Jane": 5, "Bob": 8}
        self.assertDictEqual(hiking_tracker(hikers), expected_output)


if __name__ == "__main__":
    unittest.main()
