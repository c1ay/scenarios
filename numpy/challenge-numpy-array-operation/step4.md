# Calculate Average Purchases

Write a function called `calculate_average_purchases` that takes in a NumPy array `total_purchases` and returns the following values:

- `'average_purchases_per_(customer/product)'`: A float representing the average number of purchases per (customer/product).

## Example

```python
import numpy as np

# Generate some sample transaction data
transactions = np.array([[3, 4, 1],
                         [0, 2, 5],
                         [1, 2, 2]])

# Calculate the total number of purchases by customer and by product
total_purchases_by_customer, total_purchases_by_product = calculate_purchase_totals(transactions)

# Calculate the average number of purchases per customer and per product
average_purchases_per_customer = calculate_average_purchases(total_purchases_by_customer)
average_purchases_per_product = calculate_average_purchases(total_purchases_by_product)

# Print the results
print("Average purchases per customer:", average_purchases_per_customer)
print("Average purchases per product:", average_purchases_per_product)
# Average purchases per customer: 3.0
# Average purchases per product: 2.6666666666666665

```
