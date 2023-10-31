#!/usr/bin/python3

"""
    Print a square of the character '#' with the given size.
"""


def print_square(size):
    """
    Print a square of the character '#' with the given size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0 or a float.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 or isinstance(size, float):
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
