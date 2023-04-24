import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_raises
from numpy.testing import assert_allclose
from split_array import split_array


class TestNumPyArrayOperations(unittest.TestCase):
    def test_split_array(self):
        # Test 1
        arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected1 = [
            np.array([[1, 2, 3]]),
            np.array([[4, 5, 6]]),
            np.array([[7, 8, 9]]),
        ]
        assert_array_equal(split_array(arr1, 3, axis=0), expected1)

        # Test 2
        arr2 = np.array([1, 2, 3, 4, 5, 6])
        expected2 = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6])]
        assert np.array_equal(split_array(arr2, 3, axis=0), expected2)


if __name__ == "__main__":
    unittest.main()
