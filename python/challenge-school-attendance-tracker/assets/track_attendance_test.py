import sys

sys.path.append("/home/labex/project")

import unittest
from track_attendance import track_attendance


class TestAttendanceTracker(unittest.TestCase):
    def test_track_attendance(self):
        attendance = {
            "Alice": [("2023-04-01", "P"), ("2023-04-02", "P"), ("2023-04-03", "L")],
            "Bob": [("2023-04-01", "P"), ("2023-04-02", "A"), ("2023-04-03", "A")],
            "Charlie": [("2023-04-01", "L"), ("2023-04-02", "L"), ("2023-04-03", "P")],
        }
        result = track_attendance(attendance)
        expected_result = {"Alice": 100.0, "Bob": 33.33, "Charlie": 100.0}
        self.assertAlmostEqual(result["Alice"], expected_result["Alice"], places=2)
        self.assertAlmostEqual(result["Bob"], expected_result["Bob"], places=2)
        self.assertAlmostEqual(result["Charlie"], expected_result["Charlie"], places=2)

        attendance2 = {
            "David": [("2023-04-01", "P"), ("2023-04-02", "P"), ("2023-04-03", "P")],
            "Ethan": [("2023-04-01", "P"), ("2023-04-02", "A"), ("2023-04-03", "A")],
            "Frank": [("2023-04-01", "P"), ("2023-04-02", "P"), ("2023-04-03", "L")],
        }
        result2 = track_attendance(attendance2)
        expected_result2 = {"David": 100.0, "Ethan": 33.33, "Frank": 100.0}
        self.assertAlmostEqual(result2["David"], expected_result2["David"], places=2)
        self.assertAlmostEqual(result2["Ethan"], expected_result2["Ethan"], places=2)
        self.assertAlmostEqual(result2["Frank"], expected_result2["Frank"], places=2)

        attendance3 = {
            "Grace": [("2023-04-01", "L"), ("2023-04-02", "L"), ("2023-04-03", "L")],
            "Henry": [("2023-04-01", "A"), ("2023-04-02", "A"), ("2023-04-03", "A")],
            "Isabella": [("2023-04-01", "P"), ("2023-04-02", "P"), ("2023-04-03", "P")],
        }
        result3 = track_attendance(attendance3)
        expected_result3 = {"Grace": 100.0, "Henry": 0.0, "Isabella": 100.0}
        self.assertAlmostEqual(result3["Grace"], expected_result3["Grace"], places=2)
        self.assertAlmostEqual(result3["Henry"], expected_result3["Henry"], places=2)
        self.assertAlmostEqual(
            result3["Isabella"], expected_result3["Isabella"], places=2
        )


if __name__ == "__main__":
    unittest.main()
