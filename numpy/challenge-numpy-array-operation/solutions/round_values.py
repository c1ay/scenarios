import numpy as np


def round_values(value, decimal):
    """
    Round the results to 2 decimal places

    Parameters
    ----------
    value: float
        A float that needs to be round.
    decimal: int
        The decimal places.

    Returns
    -------
    float
        A rounded float.
    """
    return np.round(value, decimal)
