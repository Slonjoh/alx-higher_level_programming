#!/usr/bin/python3
"""
    This class represents.
"""


class Square:
    """
    This class represents.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with a given size and position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints a representation of the square.
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        output = ""
        if self.size == 0:
            return ""
        for i in range(self.position[1]):
            output += "\n"
        for i in range(self.size):
            output += " " * self.position[0] + "#" * self.size + "\n"
        return output[:-1]
