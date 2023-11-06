#!/usr/bin/python3
"""
    MyInt is a custom integer class that inherits from int
"""


class MyInt(int):
    """
    MyInt is a custom integer class that inherits from int
    """
    def __eq__(self, other):
        """
        Inverts the equality operator (==).
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator (!=).
        """
        return super().__eq__(other)
