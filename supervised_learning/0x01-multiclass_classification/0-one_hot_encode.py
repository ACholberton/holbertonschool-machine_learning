#!usr/bin/env python3
""" this function converts a numeric label vector into a one-hot matrix"""


import numpy as np


def one_hot_encode(Y, classes):
    """Y is a numpy array, 
    and classes is the maximum number of classes found in Y"""

    if not isinstance(Y, np.ndarray) or len(Y) == 0:
        return None
    if not isinstance(classes, int) or classes < np.max(Y) + 1:
        return None
    A = np.zeros((classes, Y.shape[0]))
    for i, m in enumerate(Y):
        A[m][i] = 1
    return A
