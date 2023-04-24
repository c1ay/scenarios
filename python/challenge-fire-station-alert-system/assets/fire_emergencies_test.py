import sys

sys.path.append("/home/labex/project")

import unittest
from fire_emergencies import Emergency, FireStation


class TestFireStationAlertSystem(unittest.TestCase):
    def test_emergency_class(self):
        e = Emergency(2, "Main St")
        self.assertEqual(e.priority, 2)
        self.assertEqual(e.location, "Main St")

    def test_fire_station(self):
        fs = FireStation()
        e1 = Emergency(2, "Main St")
        e2 = Emergency(1, "Market St")
        fs.add_emergency(e1)
        fs.add_emergency(e2)
        fs.prioritize_emergencies()
        self.assertEqual(fs.emergencies[0], e2)
        fs.remove_emergency(e1)
        self.assertEqual(len(fs.emergencies), 1)


if __name__ == "__main__":
    unittest.main()
