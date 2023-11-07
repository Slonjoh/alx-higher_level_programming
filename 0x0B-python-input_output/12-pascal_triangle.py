#!/usr/bin/python3
"""
Generates Pascal's triangle up to the n-th row.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the n-th row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    Args:
        triangle (list of lists): The Pascal's triangle to print.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
