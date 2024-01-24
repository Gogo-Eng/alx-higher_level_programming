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

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        self._Square__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self._Square__size**2

    def my_print(self):
        if self._Square__size == 0:
            print()
        else:
            for i in range(self._Square__size):
                print(f"{'#' * self._Square__size}")
