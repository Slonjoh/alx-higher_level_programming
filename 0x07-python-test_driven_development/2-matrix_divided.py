#!/usr/bin/python3

"""
    Divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        ZeroDivisionError: If div is equal to 0.
        TypeError: If rows of the matrix have different sizes.

    """
    error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(error_1)

    if not all(all(isinstance(element, (int, float)) for element in row)
               for row in matrix):
        raise TypeError(error_1)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]
    return new_matrix
