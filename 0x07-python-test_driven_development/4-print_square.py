#!/usr/bin/python3

"""
function that prints a square with the character #
"""


def print_square(size):
    """
     function that prints a square with the character #

    Args:
        size: length of square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
