#!/usr/bin/python3
"""
Class representing basic geometry.
"""


class BaseGeometry:
    """
    Class representing basic geometry.
    """
    def area(self):
        """
        Calculate the area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
