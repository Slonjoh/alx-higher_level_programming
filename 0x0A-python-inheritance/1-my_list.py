#!/usr/bin/python3
"""
    Inherits from list and provides a method to print list sorted.
"""


class MyList(list):
    """
    Class that inherits from list and provides a method to print  list sorted.
    """

    def print_sorted(self):
        """
        Print the list sorted in ascending order.
        """
        print(sorted(self))
