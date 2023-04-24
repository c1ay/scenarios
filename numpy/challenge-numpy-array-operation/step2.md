# Calculate Total Purchases

Write a function called `calculate_total_purchases` that takes in a NumPy array `transactions` and returns following values:

- `'total_purchases_by_customer'`: A NumPy array of shape `(num_customers,)` containing the total number of purchases for each customer.
- `'total_purchases_by_product'`: A NumPy array of shape `(num_products,)` containing the total number of purchases for each product.

## Example

```python
import numpy as np

# Generate some sample transaction data
transactions = np.array([[3, 4, 1],
                         [0, 2, 5],
                         [1, 2, 2]])

# Calculate the total number of purchases by customer and by product
total_purchases_by_customer, total_purchases_by_product = calculate_purchase_totals(transactions)

# Print the results
print("Total purchases by customer:", total_purchases_by_customer)
print("Total purchases by product:", total_purchases_by_product)
# Total purchases by customer: [8 7 5]
# Total purchases by product: [4 8 8]

```
