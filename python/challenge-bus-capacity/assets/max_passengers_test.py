import sys

sys.path.append("/home/labex/project")

import unittest
from max_passengers import max_passengers


class TestMaxPassengers(unittest.TestCase):
    def test_max_passengers(self):
        buses = [(50, 30), (40, 20), (60, 45)]
        self.assertEqual(max_passengers(buses), 20)

    def test_max_passengers_all_full_buses(self):
        buses = [(50, 50), (40, 40), (60, 60)]
        self.assertEqual(max_passengers(buses), 0)

    def test_max_passengers_all_empty_buses(self):
        buses = [(50, 0), (40, 0), (60, 0)]
        self.assertEqual(max_passengers(buses), 60)

    def test_max_passengers_one_bus(self):
        buses = [(50, 30)]
        self.assertEqual(max_passengers(buses), 20)


if __name__ == "__main__":
    unittest.main()
