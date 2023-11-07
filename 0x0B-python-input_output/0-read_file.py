#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Read and print the content of a text file to stdout.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')
