import numpy as np


def calculate_covariance_matrix(weights: np.ndarray, heights: np.ndarray) -> np.ndarray:
    """
    Calculate the covariance matrix of the data using NumPy's dot function.

    Parameters:
    weights (np.ndarray): A NumPy array of shape (n_samples, 1) representing the weights of the individuals
    heights (np.ndarray): A NumPy array of shape (n_samples, 1) representing the heights of the individuals

    Returns:
    np.ndarray: A NumPy array of shape (2, 2) representing the covariance matrix of the data.
    """
    # TODO: implement this function
    # Subtract the mean from the data

    # Calculate the covariance matrix
