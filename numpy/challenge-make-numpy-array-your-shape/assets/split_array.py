import numpy as np
from typing import List, Union, Optional


def split_array(
    arr: np.ndarray,
    indices_or_sections: Union[int, List[int]],
    axis: Optional[int] = None,
) -> List[np.ndarray]:
    """
    Split an array into multiple sub-arrays along a specified axis.

    Parameters:
        arr (np.ndarray): Input array to be split
        indices_or_sections (Union[int, List[int]]): If an integer, specifies the number of equally-sized sub-arrays
            to be created along the specified axis. If a list of integers, specifies the indices at which to split the array.
        axis (Optional[int]): Axis along which to split the array. Default is None, which means the array is flattened before splitting.

    Returns:
        List[np.ndarray]: List of sub-arrays created by splitting the input array

    Raises:
        ValueError: If the number of sections in the list is not compatible with the size of the array along the specified axis
    """
    # TODO: Implement this function.
    # Note: Do not change the existing code
    result = None
    return result
