# Set Intersection

Write a Python function named `set_intersection(set1: set, set2: set) -> set` that takes in two sets `set1` and `set2` and returns a new set containing the elements that are present in both `set1` and `set2`.

## Constraints

Input

- `set1` (0 <= len(set1) <= 10^6) : A set containing unique elements.
- `set2` (0 <= len(set2) <= 10^6) : A set containing unique elements.

Output

- Returns a new set containing the elements that are present in both set1 and set2.

### Example

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result_set = set_intersection(set1, set2)
print(result_set) # Output: {4, 5}
```
