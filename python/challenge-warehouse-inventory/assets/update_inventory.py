def update_inventory(inventory, orders):
    """
    Update the inventory based on the new orders and return the updated inventory.

    Parameters:
    inventory (dict): Current inventory of the warehouse where the keys are the item names and the values are the quantities in stock.
    orders (list of tuples): New orders that need to be fulfilled where each tuple contains the following information:
        - the item name
        - the quantity ordered
        - the location where the item is stored

    Returns:
    dict: Updated inventory.

    """
    # Write your code here
