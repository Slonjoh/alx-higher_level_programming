#!/usr/bin/python3
"""
    This class represents a square.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new square.
        area(self): Computes the area of the square.
        my_print(self): Prints a representation of the square.
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

    def my_print(self):
        """
        Prints a representation of the square.

        If d size is 0, it prints empty line. else prints d square using '#'.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
