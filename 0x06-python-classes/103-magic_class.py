#!/usr/bin/python3
"""
    This class reps a MagicClass with radius attributes 4 geometric cals.
"""


import math
"""
Imports math to be used
"""


class MagicClass:
    """
    This class reps a MagicClass with radius attributes 4 geometric cals.

    Attributes:
        __radius (float or int): The radius of the MagicClass instance.

    Methods:
        __init__(self, radius=0): Init a new MagicClass with optional radius.
        area(self): Calculate the area of the MagicClass instance.
        circumference(self): Cal d circumference of d MagicClass instance.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass with an optional radius.

        Args:
            radius (int or float, optional):radius of the MagicClass instance.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the MagicClass instance.

        Returns:
            float: The area of the MagicClass instance.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the MagicClass instance.

        Returns:
            float: The circumference of the MagicClass instance.
        """
        return 2 * math.pi * self.__radius
