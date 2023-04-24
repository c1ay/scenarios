# School Enrollment System

Write a Python function called `count_enrollment` that takes a list of integers as input and returns a dictionary with the number of students enrolled in each grade level. The input list will contain integers between 1 and 12, representing the grade levels of students. The output dictionary should have keys from 1 to 12, and the values should be the number of students enrolled in each grade level.

## Example Usage

```python
enrollment_list = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 10, 10, 11, 12]

enrollment_dict = count_enrollment(enrollment_list)

print(enrollment_dict) # Output: {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 1, 8: 3, 9: 2, 10: 2, 11: 1, 12: 1}
```

## TODO

- Complete `count_enrollment.py`

## Requirements

- The `count_enrollment` function should take a single argument (the list of integers).
- The `count_enrollment` function should return a dictionary with keys from 1 to 12, and values representing the number of students enrolled in each grade level.
- If a grade level does not have any enrolled students, the corresponding value in the output dictionary should be 0.
