#!/usr/bin/python3
"""
Program returns dictionary description with simple data structure for JSON.
"""


def class_to_json(obj):
    """
    Returns a dictionary description for JSON serialization of an object.
    """
    attributes = obj.__dict__
    serializable_attributes = {
            key: value
            for key, value in attributes.items()
            if not callable(value) and not key.startswith("_")
            }

    return serializable_attributes
