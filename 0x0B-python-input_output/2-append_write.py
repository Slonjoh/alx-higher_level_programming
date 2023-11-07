#!/usr/bin/python3
"""
Program appends string at end of a text file & returns num of chars added.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file & returns num of chars added.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
