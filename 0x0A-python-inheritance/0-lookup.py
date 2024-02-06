#!/usr/bin/python3

"""
 returns the list of attributes and methods of an object
"""


def lookup(obj):
    """returns the list of attributes and methods of an object:

    Args:
        obj: the object of the class

    Returns:
        Returns a list object
    """

    return dir(obj)
