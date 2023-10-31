#!/usr/bin/python3

"""
    Print the name in the format "My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the name in the format "My name is <first name> <last name>."

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    """

    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name must be a string" if not isinstance
                        (first_name, str) else "last_name must be a string")

    first_name = first_name.strip()
    last_name = last_name.strip()

    if first_name or last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print("My name is")
