#!/usr/bin/python3
"""
Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherited class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")


s = Square(13)

print(s)
print(s.area())
