# Reshape an Array

## TODO

Write a function `reshape_array(arr: np.ndarray, new_shape: tuple) -> np.ndarray` that takes in an array `arr` and a new shape `new_shape`, and returns a new NumPy array with the same data but a new shape. If the new shape is not compatible with the number of elements in the original array, raise a `ValueError`.

For example:

```python
>>> arr = np.array([[1, 2, 3], [4, 5, 6]])
>>> reshape_array(arr, (3, 2))
array([[1, 2],
       [3, 4],
       [5, 6]])

>>> reshape_array(arr, (3, 3)) # Raises ValueError
```
