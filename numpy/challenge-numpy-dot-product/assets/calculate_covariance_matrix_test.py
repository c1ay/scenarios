import sys

sys.path.append("/home/labex/project")

import numpy as np
import unittest
from calculate_covariance_matrix import calculate_covariance_matrix


class TestCalculateCovarianceMatrix(unittest.TestCase):
    def test_covariance_matrix(self):
        weights = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140]).reshape(-1, 1)
        heights = np.array([1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]).reshape(
            -1, 1
        )

        covariance_matrix = calculate_covariance_matrix(weights, heights)
        print(covariance_matrix)

        self.assertEqual(covariance_matrix.shape, (2, 2))
        self.assertTrue(
            np.allclose(
                covariance_matrix, np.array([[8.25e02, 8.25e0], [8.25e0, 8.25e-02]])
            )
        )


if __name__ == "__main__":
    unittest.main()
