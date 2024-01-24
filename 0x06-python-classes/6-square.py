#!/usr/bin/python3
"""
class Square: a class Square that defines a square by
"""


class Square:
    """
    a class Square that defines a square by
    """

    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._Gogo = position
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

    @property
    def position(self):
        return self._Gogo

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__Gogo = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if self._Square__size == 0:
            print()
            return

        for i in range(self._Gogo[1]):
            print()

        for i in range(self._Square__size):
            print("{}{}".format(" " * self._Gogo[0], "#" * self._Square__size))
