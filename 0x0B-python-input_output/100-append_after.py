#!/usr/bin/python3
"""
Inserts new_string after each line containing search_string in the file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts new_string after each line containing search_string in the file.
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
