# Postal Service

Write a Python program that generates unique postal codes for new customers based on the following rules:

- The first three digits must be between 100 and 999, inclusive.
- The last two digits must be between 01 and 99, inclusive.
- The program should keep track of all previously generated postal codes to ensure uniqueness.
- The program should be able to generate a specified number of postal codes.

## Example Usage

```python
# Generate 5 postal codes
>>> generate_postal_codes(5)
[12345, 23456, 34567, 45678, 56789]

# Generate 10 postal codes
>>> generate_postal_codes(10)
[67890, 78901, 89012, 90123, 12349, 23458, 34567, 45676, 56785, 67894]
```

## TODO

- Complete `generate_postal_codes.py`

## Requirements

- The program must have the following function:
  - `generate_postal_codes(n)`: Generates `n` unique postal codes and returns them as a list.
- The program must use a loop and the `range()` function to generate the postal codes.
- The program should store the generated postal codes in a list and check for uniqueness before adding them to the list.
