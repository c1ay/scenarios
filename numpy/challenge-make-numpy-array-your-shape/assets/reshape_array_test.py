import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_raises
from numpy.testing import assert_allclose
from reshape_array import reshape_array


class TestNumPyArrayOperations(unittest.TestCase):
    def test_reshape_array(self):
        # Test 1
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        expected1 = np.array([[1, 2], [3, 4], [5, 6]])
        assert_array_equal(reshape_array(arr1, (3, 2)), expected1)

        # Test 2
        arr2 = np.array([[1, 2], [3, 4], [5, 6]])
        expected2 = np.array([1, 2, 3, 4, 5, 6])
        assert_array_equal(reshape_array(arr2, (6,)), expected2)

        # Test 3
        arr3 = np.array([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            reshape_array(arr3, (2, 2))


if __name__ == "__main__":
    unittest.main()
