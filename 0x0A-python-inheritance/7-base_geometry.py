#!/usr/bin/python3
"""
 empty class BaseGeometry
"""


class BaseGeometry:
    """
     empty class BaseGeometry
    """
    pass

    def area(self):
        print("GOGo")
        # raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value is True:
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
