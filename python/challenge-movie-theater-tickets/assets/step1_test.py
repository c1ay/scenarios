import sys

sys.path.append("/home/labex/project")
import unittest
from step1 import calculate_ticket_price


class TestTicketPrice(unittest.TestCase):
    def test_negative_age(self):
        with self.assertRaises(ValueError):
            calculate_ticket_price(-5, "12:00")

    def test_invalid_show_time(self):
        with self.assertRaises(ValueError):
            calculate_ticket_price(30, "25:00")
            calculate_ticket_price(30, "12:60")
            calculate_ticket_price(30, "12:00:00")
            calculate_ticket_price(30, "12")

    def test_morning_show(self):
        self.assertEqual(calculate_ticket_price(30, "10:30"), 10)

    def test_afternoon_show_adult(self):
        self.assertEqual(calculate_ticket_price(30, "14:30"), 15)

    def test_afternoon_show_child(self):
        self.assertEqual(calculate_ticket_price(10, "14:30"), 10)

    def test_evening_show_adult(self):
        self.assertEqual(calculate_ticket_price(30, "18:30"), 20)

    def test_evening_show_child(self):
        self.assertEqual(calculate_ticket_price(10, "18:30"), 15)


if __name__ == "__main__":
    unittest.main()
