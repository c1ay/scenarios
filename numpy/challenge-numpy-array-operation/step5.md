# Round Values

Write a function called `round_values` that rounds the values to 2 decimal places.

## Example

```python
import numpy as np

# Calculate the average number of purchases per customer and per product
average_purchases_per_customer = calculate_average_purchases(total_purchases_by_customer)
average_purchases_per_product = calculate_average_purchases(total_purchases_by_product)

# Round the results to 2 decimal places
average_purchases_per_customer = round_values(average_purchases_per_customer, 2)
average_purchases_per_product = round_values(average_purchases_per_product, 2)

# Print the rounded results
print("Average purchases per customer (rounded to 2 decimal places):", average_purchases_per_customer)
print("Average purchases per product (rounded to 2 decimal places):", average_purchases_per_product)

# Average purchases per customer (rounded to 2 decimal places): 3.0
# Average purchases per product (rounded to 2 decimal places): 2.67

```
