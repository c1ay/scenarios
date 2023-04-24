import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_raises
from numpy.testing import assert_allclose
from concatenate_arrays import concatenate_arrays


class TestNumPyArrayOperations(unittest.TestCase):
    def test_concatenate_arrays(self):
        # Test 1
        arr1 = np.array([[1, 2], [3, 4]])
        arr2 = np.array([[5, 6], [7, 8]])
        expected1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        assert_array_equal(concatenate_arrays(arr1, arr2, axis=0), expected1)

        # Test 2
        arr3 = np.array([[1, 2], [3, 4]])
        arr4 = np.array([[5, 6], [7, 8]])
        expected2 = np.array([[1, 2, 5, 6], [3, 4, 7, 8]])
        assert_array_equal(concatenate_arrays(arr3, arr4, axis=1), expected2)


if __name__ == "__main__":
    unittest.main()
