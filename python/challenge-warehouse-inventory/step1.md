# Warehouse Inventory

Your task is to write a Python function called `update_inventory` that takes in two parameters:

- `inventory` (a dictionary): represents the current inventory of the warehouse where the keys are the item names and the values are the quantities in stock.
- `orders` (a list of tuples): represents the new orders that need to be fulfilled where each tuple contains the following information:
  - the item name
  - the quantity ordered
  - the location where the item is stored

The function should update the inventory based on the new orders and return the updated inventory.

## Example Usage

```python
inventory = {"apple": 10, "banana": 20, "orange": 30}
orders = [("apple", 5, "A1"), ("banana", 10, "B2"), ("pear", 5, "C3")]

updated_inventory = update_inventory(inventory, orders)
print(updated_inventory)
```

Output:

```python
Order for 'apple' at location 'A1' was successful.
Order for 'banana' at location 'B2' was successful.
Order for 'pear' cannot be fulfilled as the item is not in stock.
{'apple': 5, 'banana': 10, 'orange': 30}
```

## TODO

- Complete `update_inventory.py`

## Requirements

- The function should handle cases where the item is not in the inventory or the quantity ordered is greater than the quantity in stock.
- The function should print out a message for each order indicating whether the order was successful or not.
