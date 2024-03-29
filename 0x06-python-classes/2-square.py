#!/usr/bin/python3
"""
class Square: a class Square that defines a square by
"""


class Square:
    """
    a class Square that defines a square by
    """
    def __init__(self, size=0):
        self._Square__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
