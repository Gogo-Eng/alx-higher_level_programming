#!/usr/bin/python3
"""
returns True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """

    Args:
        obj: an object
        a_class: a class

    Returns:
        _True
    """
    return type(obj) is a_class
