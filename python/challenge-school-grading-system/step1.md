# School Grading System

Write a Python function called `calculate_grade` that takes a dictionary of student information as input and returns the final grade for that student. The student information dictionary will have the following keys:

- `"name"` (string): the student's name
- `"assignments"` (list of integers): the student's grades for various assignments (out of 100)
- `"tests"` (list of integers): the student's grades for various tests (out of 100)
- `"attendance"` (integer): the student's attendance record (out of 100)

The final grade should be calculated as follows:

- Assignments are worth 50% of the final grade
- Tests are worth 40% of the final grade
- Attendance is worth 10% of the final grade

The final grade should be rounded to the nearest whole number.

## Example Usage

```python
student_info = {
    "name": "John Smith",
    "assignments": [90, 85, 75, 100],
    "tests": [80, 85],
    "attendance": 90
}

final_grade = calculate_grade(student_info)

print(final_grade) # Output: 93
```

## TODO

- Complete `calculate_grade.py`

## Requirements

- The `calculate_grade` function should take a single argument (the student information dictionary).
- The `calculate_grade` function should return a single integer (the final grade).
- Use the `max` function to find the highest grade for assignments and tests.
