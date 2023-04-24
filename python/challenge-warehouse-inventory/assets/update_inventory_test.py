import sys

sys.path.append("/home/labex/project")

import unittest
from update_inventory import update_inventory


class TestUpdateInventory(unittest.TestCase):
    def test_update_inventory(self):
        inventory = {"apple": 10, "banana": 20, "orange": 30}
        orders = [("apple", 5, "A1"), ("banana", 10, "B2"), ("pear", 5, "C3")]
        expected_output = {"apple": 5, "banana": 10, "orange": 30}
        self.assertEqual(update_inventory(inventory, orders), expected_output)

        inventory = {"apple": 10, "banana": 20, "orange": 30}
        orders = [("apple", 5, "A1"), ("banana", 30, "B2"), ("pear", 5, "C3")]
        expected_output = {"apple": 5, "banana": 20, "orange": 30}
        self.assertEqual(update_inventory(inventory, orders), expected_output)

        inventory = {"apple": 10, "banana": 20, "orange": 30}
        orders = [("peach", 5, "A1"), ("banana", 10, "B2"), ("pear", 5, "C3")]
        expected_output = {"apple": 10, "banana": 10, "orange": 30}
        self.assertEqual(update_inventory(inventory, orders), expected_output)


if __name__ == "__main__":
    unittest.main()
