#!/usr/bin/python3
"""
Check if obj inherits from a_class (directly or indirectly).
"""


def inherits_from(obj, a_class):
    """
    Check if obj inherits from a_class (directly or indirectly).
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
