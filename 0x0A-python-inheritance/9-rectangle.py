#!/usr/bin/python3
"""
Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherited class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__deep = width
        self.__long = height

    def area(self):
        return self.__deep * self.__long

    def __str__(self):
        return (f"[Rectangle] {self.__deep}/{self.__long}")
