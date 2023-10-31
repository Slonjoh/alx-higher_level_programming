#!/usr/bin/python3

"""
    Print a text with 2 new lines after each of the characters: ., ? and :.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of the characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    n = "".join([c if c not in "?.:" else c + "\n\n" for c in text])
    print("\n".join([line.strip() for line in n.split("\n")]), end="")
