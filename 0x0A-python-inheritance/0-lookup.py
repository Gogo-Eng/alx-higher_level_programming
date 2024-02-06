#!/usr/bin/python3

"""
 function that returns the list of available attributes and methods of an object
"""

def lookup(obj):
    """function that returns the list of available attributes and methods of an object:

    Args:
        obj: the object of the class

    Returns:
        Returns a list object
    """
    
    return dir(obj)
        