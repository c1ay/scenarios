import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from calculate_purchase_totals import calculate_purchase_totals
from calculate_revenue_totals import calculate_revenue_totals


class TestCalculateRevenueTotals(unittest.TestCase):
    def test_calculate_revenue_totals(self):
        transactions = np.array([[1, 2, 3], [0, 1, 0], [4, 0, 2]])
        prices = 10
        (
            total_purchases_by_customer,
            total_purchases_by_product,
        ) = calculate_purchase_totals(transactions)
        print(total_purchases_by_customer, total_purchases_by_product)
        expected_total_revenue_by_customer = np.array([60, 10, 60])
        expected_total_revenue_by_product = np.array([50, 30, 50])
        total_revenue_by_customer, total_revenue_by_product = calculate_revenue_totals(
            total_purchases_by_customer, total_purchases_by_product, prices
        )
        np.testing.assert_array_equal(
            total_revenue_by_customer, expected_total_revenue_by_customer
        )
        np.testing.assert_array_equal(
            total_revenue_by_product, expected_total_revenue_by_product
        )


if __name__ == "__main__":
    unittest.main()
