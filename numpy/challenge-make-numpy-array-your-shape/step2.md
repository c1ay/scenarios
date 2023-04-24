# Concatenate Arrays

### TODO

Write a function `concatenate_arrays(arr1: np.ndarray, arr2: np.ndarray, axis: int) -> np.ndarray` that takes in two NumPy arrays `arr1` and `arr2` and an axis along which to concatenate the arrays. The function should return a new NumPy array that is the concatenation of the two input arrays along the specified axis.

For example:

```python
>>> arr1 = np.array([[1, 2], [3, 4]])
>>> arr2 = np.array([[5, 6], [7, 8]])
>>> concatenate_arrays(arr1, arr2, axis=0)
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])

>>> concatenate_arrays(arr1, arr2, axis=1)
array([[1, 2, 5, 6],
       [3, 4, 7, 8]])
```
