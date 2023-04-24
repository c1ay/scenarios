import sys

sys.path.append("/home/labex/project")
import numpy as np
import unittest
from customer_stats import customer_stats


class TestCustomerStats(unittest.TestCase):
    def test_customer_stats(self):
        transactions = np.array([[1, 2, 3], [0, 1, 0], [4, 0, 2]])
        result = customer_stats(transactions)
        expected_result = {
            "total_purchases_by_customer": np.array([6, 1, 6]),
            "total_purchases_by_product": np.array([5, 3, 5]),
            "total_revenue_by_customer": np.array([60, 10, 60]),
            "total_revenue_by_product": np.array([50, 30, 50]),
            "average_purchases_per_customer": 4.33,
            "average_purchases_per_product": 4.33,
        }
        # Convert NumPy arrays to lists
        for key in expected_result:
            if isinstance(expected_result[key], np.ndarray):
                expected_result[key] = expected_result[key].tolist()
            if isinstance(result[key], np.ndarray):
                result[key] = result[key].tolist()
        self.assertDictEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
