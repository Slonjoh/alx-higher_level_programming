#!/usr/bin/python3

"""
    Multiply two matrices using NumPy.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        ndarray: The resulting matrix after multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    """
    a = np.array(m_a)
    b = np.array(m_b)

    result = np.dot(a, b)

    return result
