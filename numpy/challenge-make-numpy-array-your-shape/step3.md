# Stack Arrays

### TODO

Write a function `stack_arrays(arr1: np.ndarray, arr2: np.ndarray, axis: int) -> np.ndarray` that takes in two NumPy arrays `arr1` and `arr2` and an axis along which to stack the arrays. The function should return a new NumPy array that is the stacked version of the two input arrays along the specified axis.

For example:

```python
>>> arr1 = np.array([1, 2, 3])
>>> arr2 = np.array([4, 5, 6])
>>> stack_arrays(arr1, arr2, axis=0)
array([[1, 2, 3],
       [4, 5, 6]])

>>> stack_arrays(arr1, arr2, axis=1)
array([[1, 4],
       [2, 5],
       [3, 6]])
```
