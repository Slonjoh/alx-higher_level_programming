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
        __init__(self, size): Init a new instance of d Square class with size.
        area(self): Calculates and returns the area of the square.
    """
    def __init__(self, size=0):

        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a negative integer.
        """

        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.

        Raises:
            None
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size * self.__size
