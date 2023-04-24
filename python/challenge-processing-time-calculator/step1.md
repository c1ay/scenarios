# Immigration Office Processing Time Calculator

Your task is to write a Python function called `calculate_processing_time` that takes in one parameter.The function should calculate the processing time for the application based on the following formula:

- If the number of pages is less than or equal to 10, the processing time is 1 day.
- If the number of pages is greater than 10 and less than or equal to 50, the processing time is 3 days.
- If the number of pages is greater than 50 and less than or equal to 100, the processing time is 5 days.
- If the number of pages is greater than 100, the processing time is 7 days.

The function should return the processing time in days.

## Example Usage

```python
num_pages = 25

processing_time = calculate_processing_time(num_pages)
print(processing_time)
```

Output:

```python
3
```

```python
num_pages = 150

processing_time = calculate_processing_time(num_pages)
print(processing_time)
```

Output:

```python
7
```

## TODO

- Complete `calculate_processing_time.py`

## Requirements

- `num_pages` (an integer): represents the number of pages in the application.
- The function should calculate the processing time for the application based on the number of pages in the application using the formula described above.
- The function should return the processing time in days.
