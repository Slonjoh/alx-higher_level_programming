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
        __init__(self, size): Init new instance of d Square class with d size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): Size of the square. It must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a negative integer.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """

        return self.__size * self.__size
