# Movie Theater Tickets

## Problem Description

You need to create a Python program that sells tickets to customers based on their age and the time of day. The theater has the following pricing rules:

- Morning show (before 12pm): \$10 for everyone
- Afternoon show (12pm to 5pm): \$15 for adults (age >= 18) and \$10 for children (age < 18)
- Evening show (after 5pm): \$20 for adults (age >= 18) and \$15 for children (age < 18)

## Requirements

- Define a function `calculate_ticket_price(age: int, show_time: str) -> int` that takes in the age of the customer (an integer) and the time of the show (a string in the format 'HH:MM') and returns the price of the ticket (an integer).
- The function should handle invalid show times and raise a `ValueError`.
- The function should handle invalid ages (negative values) and raise a `ValueError`.
- Use a dictionary to store the pricing rules for each show time.

## Example Usage

```
calculate_ticket_price(25, '10:30')  # Output: 10
calculate_ticket_price(16, '14:30')  # Output: 10
calculate_ticket_price(30, '18:30')  # Output: 20
calculate_ticket_price(10, '18:30')  # Output: 15
```
