import numpy as np


def calculate_average_purchases(total_purchases: np.ndarray) -> float:
    """
    Calculate the average number of purchases per customer or per product.

    Parameters
    ----------
    total_purchases : np.ndarray
        A 1D NumPy array of shape (num_customers,) or (num_products,) containing the total number of purchases for each
        customer or product.

    Returns
    -------
    float
        The average number of purchases per customer or per product.
    """
    # implementation goes here
