import numpy as np
from typing import List, Union, Optional


def concatenate_arrays(arr1: np.ndarray, arr2: np.ndarray, axis: int) -> np.ndarray:
    """
    Concatenate two arrays along a specified axis.

    Parameters:
        arr1 (np.ndarray): First input array to be concatenated
        arr2 (np.ndarray): Second input array to be concatenated
        axis (int): Axis along which to concatenate the arrays

    Returns:
        np.ndarray: Concatenated array
    """
    return np.concatenate((arr1, arr2), axis=axis)
