# Split an Array

### TODO

Write a function `split_array(arr: np.ndarray, indices_or_sections: Union[int, List[int]], axis: Optional[int] = None) -> List[np.ndarray]` that takes in a NumPy array `arr`, an integer `indices_or_sections`, and an optional axis `axis`. The function should return a list of NumPy arrays that are the splits of the input array along the specified axis. If the input integer `indices_or_sections` is a scalar, the input array will be split into equally sized chunks along the specified axis. If `indices_or_sections` is a list of integers, the input array will be split into the specified sections along the specified axis.

For example:

```python
>>> arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> split_array(arr, 3, axis=0)
[array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]

>>> split_array(arr, 2, axis=1)
[array([[1, 2],
        [4, 5],
        [7, 8]]),
 array([[3],
        [6],
        [9]])]

>>> split_array(arr, [1, 2], axis=0)
[array([[1, 2, 3]]), array([[4, 5, 6], [7, 8, 9]])]
```
