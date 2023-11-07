#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8) and returns characters.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
