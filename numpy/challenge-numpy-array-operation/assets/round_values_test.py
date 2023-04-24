import sys

sys.path.append("/home/labex/project")
import unittest
import numpy as np
from round_values import round_values


class TestRounding(unittest.TestCase):
    def test_rounding(self):
        # Define some example inputs
        average_purchases_per_customer = 3.141592653589793
        average_purchases_per_product = 2.6666666666666665

        # Round the inputs to 2 decimal places
        rounded_average_purchases_per_customer = round_values(
            average_purchases_per_customer, 2
        )
        rounded_average_purchases_per_product = round_values(
            average_purchases_per_product, 2
        )

        # Check that the rounded values are correct
        self.assertEqual(rounded_average_purchases_per_customer, 3.14)
        self.assertEqual(rounded_average_purchases_per_product, 2.67)


if __name__ == "__main__":
    unittest.main()
