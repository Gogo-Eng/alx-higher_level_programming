#!/usr/bin/python3
"""
 a class MyInt that inherits from int
"""


class MyInt(int):
    """

    Args:
        int: the class we are inheriting from
    """

    def __eq__(self, num):
        return self.real != num

    def __ne__(self, num):
        return self.real == num
