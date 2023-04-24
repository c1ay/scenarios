import numpy as np
from typing import List, Union, Optional


def reshape_array(arr: np.ndarray, new_shape: tuple) -> np.ndarray:
    """
    Reshape an array to a new shape.

    Parameters:
        arr (np.ndarray): Input array to be reshaped
        new_shape (tuple): Desired shape of the array

    Returns:
        np.ndarray: Reshaped array

    Raises:
        ValueError: If the new shape is not compatible with the number of elements in the original array
    """
    if np.prod(arr.shape) != np.prod(new_shape):
        raise ValueError(
            "New shape is not compatible with number of elements in input array"
        )
    result = np.reshape(arr, new_shape)
    return result
