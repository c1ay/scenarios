# School Attendance Tracker

Write a Python function `track_attendance` that accepts a dictionary of student names as keys and a list of attendance records as values. Each attendance record is a tuple of two elements: the date (in the format $YYYY-MM-DD$) and the attendance status ($P$ for present, $A$ for absent, or $L$ for late).

The function should return a dictionary containing the attendance percentage for each student for the given month.

## Example Usage

```python
attendance = {
    'Alice': [('2023-04-01', 'P'), ('2023-04-02', 'P'), ('2023-04-03', 'L')],
    'Bob': [('2023-04-01', 'P'), ('2023-04-02', 'A'), ('2023-04-03', 'A')],
    'Charlie': [('2023-04-01', 'L'), ('2023-04-02', 'L'), ('2023-04-03', 'P')]
}

print(track_attendance(attendance))
```

Output:

```python
{'Alice': 100.0,
 'Bob': 33.33,
 'Charlie': 100.0}
```

## TODO

- Complete `track_attendance.py`

## Requirements

- The function should accept a dictionary as its only argument.
- The dictionary should have student names as keys and a list of attendance records as values.
- The percentage should be rounded to two decimal places.
