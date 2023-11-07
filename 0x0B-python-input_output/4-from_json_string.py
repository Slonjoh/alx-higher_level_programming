#!/usr/bin/python3
"""
Function that returns object(Python data structure) represented by JSON string
"""


import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string.
    """
    return json.loads(my_str)
