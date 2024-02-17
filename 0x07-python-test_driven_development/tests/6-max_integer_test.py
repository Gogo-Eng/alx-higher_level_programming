#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

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
        self.assertEqual(max_integer([10, 3, 4, 2]), 10)
