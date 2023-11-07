#!/usr/bin/python3


"""
That creates an Object from a “JSON file”.
"""


def load_from_json_file(filename):
    """
    That creates an Object from a “JSON file”.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
