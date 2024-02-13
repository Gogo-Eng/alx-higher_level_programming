#!/usr/bin/python3
"""Defines argument integer """



def add_integer(a, b=98):
    """

    Args:
        a an interger or float object
        b an interger or float object

    Raises:
        TypeError: tells if a is an integer
        TypeError: tells if b is an integer

    Returns:
        Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)



print(add_integer(4, "School"))