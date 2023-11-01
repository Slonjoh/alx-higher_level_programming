#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function
    """
    def test_positive_numbers(self):
        """
        Test max_integer with a list of positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """
        Test max_integer with a list of negative numbers
        """
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """
        Test max_integer with a list of mixed numbers
        """
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        """
        Test max_integer with an empty list
        """
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
