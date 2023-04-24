def update_inventory(inventory, orders):
    # go through each item in the list of orders
    for item, quantity, location in orders:
        # check if the item is not in the inventory
        if item not in inventory:
            # print a message that the order cannot be fulfilled
            print(
                f"Order for '{item}' cannot be fulfilled as the item is not in stock."
            )
        # check if there is not enough quantity of the item in the inventory
        elif inventory[item] < quantity:
            # print a message that the order cannot be fulfilled due to insufficient stock
            print(
                f"Order for '{item}' at location '{location}' cannot be fulfilled due to insufficient stock."
            )
        else:
            # reduce the quantity of the item in the inventory by the quantity in the order
            inventory[item] -= quantity
            # print a message that the order was successful
            print(f"Order for '{item}' at location '{location}' was successful.")

    # return the updated inventory
    return inventory
