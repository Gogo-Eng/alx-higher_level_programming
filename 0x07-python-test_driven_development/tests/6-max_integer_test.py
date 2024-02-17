#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

"""
A class for performing unittest testing
"""


class TestMax_interger(unittest.TestCase):

    """
    A class for performing unittest testing
    """

    def test_max_integer(self):
        """
        class method
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
