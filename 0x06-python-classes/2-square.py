#!/usr/bin/python3
"""
    This is the Square class.

    It represents a square and initializes its size.
"""


class Square:
    """
    This is the Square class.

    It represents a square and initializes its size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Init  new instance of d class with given size.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): size of the square. It must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a negative integer.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
