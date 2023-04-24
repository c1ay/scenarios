from typing import Tuple
import numpy as np


def calculate_purchase_totals(
    transactions: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate the total number of purchases for each customer and product.

    Parameters
    ----------
    transactions : np.ndarray
        A 2D NumPy array of shape (num_customers, num_products) containing the number of purchases made by each
        customer for each product.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        A tuple containing the following two NumPy arrays:
            - total_purchases_by_customer : np.ndarray
                A 1D NumPy array of shape (num_customers,) containing the total number of purchases for each customer.
            - total_purchases_by_product : np.ndarray
                A 1D NumPy array of shape (num_products,) containing the total number of purchases for each product.
    """

    # Calculate the total number of purchases for each customer and product
    total_purchases_by_customer = np.sum(transactions, axis=1)
    total_purchases_by_product = np.sum(transactions, axis=0)

    return total_purchases_by_customer, total_purchases_by_product
