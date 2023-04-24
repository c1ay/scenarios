import sys

sys.path.append("/home/labex/project")

import unittest
import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_raises
from numpy.testing import assert_allclose
from stack_arrays import stack_arrays


class TestNumPyArrayOperations(unittest.TestCase):
    def test_stack_arrays(self):
        # Test 1
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        expected1 = np.array([[1, 2, 3], [4, 5, 6]])
        assert_array_equal(stack_arrays(arr1, arr2, axis=0), expected1)

        # Test 2
        arr3 = np.array([1, 2, 3])
        arr4 = np.array([4, 5, 6])
        expected2 = np.array([[1, 4], [2, 5], [3, 6]])
        assert_array_equal(stack_arrays(arr3, arr4, axis=1), expected2)


if __name__ == "__main__":
    unittest.main()
