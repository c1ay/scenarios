import sys

sys.path.append("/home/labex/project")
import unittest
import numpy as np
from calculate_purchase_totals import calculate_purchase_totals


class TestCalculatePurchaseTotals(unittest.TestCase):
    def test_calculate_purchase_totals(self):
        # Generate some sample transaction data
        transactions = np.array([[3, 4, 1], [0, 2, 5], [1, 2, 2]])

        # Calculate the total number of purchases by customer and by product
        (
            total_purchases_by_customer,
            total_purchases_by_product,
        ) = calculate_purchase_totals(transactions)

        # Check that the shape of the output arrays is correct
        self.assertEqual(total_purchases_by_customer.shape, (3,))
        self.assertEqual(total_purchases_by_product.shape, (3,))

        # Check that the calculated values are correct
        np.testing.assert_array_equal(total_purchases_by_customer, np.array([8, 7, 5]))
        np.testing.assert_array_equal(total_purchases_by_product, np.array([4, 8, 8]))


if __name__ == "__main__":
    unittest.main()
