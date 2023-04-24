import sys

sys.path.append("/home/labex/project")

import numpy as np
import unittest
from calculate_purchase_totals import calculate_purchase_totals
from calculate_average_purchases import calculate_average_purchases


class TestCalculateAveragePurchases(unittest.TestCase):
    def setUp(self):
        # Generate some sample transaction data
        self.transactions = np.array([[1, 2, 3], [0, 1, 0], [4, 0, 2]])

        # Calculate the total number of purchases by customer and by product
        (
            self.total_purchases_by_customer,
            self.total_purchases_by_product,
        ) = calculate_purchase_totals(self.transactions)

    def test_average_purchases_per_customer(self):
        # Calculate the average number of purchases per customer
        average_purchases_per_customer = calculate_average_purchases(
            self.total_purchases_by_customer
        )

        # Verify the result
        self.assertAlmostEqual(average_purchases_per_customer, 4.33, places=2)

    def test_average_purchases_per_product(self):
        # Calculate the average number of purchases per product
        average_purchases_per_product = calculate_average_purchases(
            self.total_purchases_by_product
        )

        # Verify the result
        self.assertAlmostEqual(average_purchases_per_product, 4.33, places=2)


if __name__ == "__main__":
    unittest.main()
