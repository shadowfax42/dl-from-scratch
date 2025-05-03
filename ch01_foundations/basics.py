import numpy as np


def square_function(x: np.ndarray) -> np.ndarray:
    """ Takes an input array and returns the square of each of its elements

    Args:
        x (np.ndarray): input array

    Returns:
        np.ndarray: output array (x squared)
    """

    return np.power(x, 2)
