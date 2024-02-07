#!/usr/bin/python3
"""
returns True if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """

    Args:
        obj: the object
        a_class: the class

    Returns:
        returns True

    """
    return type(obj) is not a_class and isinstance(obj, a_class)
