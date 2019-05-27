#!/usr/bin/python3
"""Module to find the max integer ([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test start
    """
    def test_integer(self):
        list_t = [5, 7, 10, 33, 5]
        self.assertEqual(33, max_integer(list_t))

    def test_integer(self):
        list_t = []
        self.assertEqual(None, max_integer(list_t))

    def test_neg(self):
        list_t = [-5, -7, -10, -33, -4]
        self.assertEqual(-4, max_integer(list_t))

    def test_tup(self):
        list_t = (5, 8)
        self.assertEqual(8, max_integer(list_t))

    def test_integer(self):
        list_t = [5.9, 7.5, 1.0, 3.3]
        self.assertEqual(7.5, max_integer(list_t))

    def test_integer(self):
        list_t = [5, "holberton", 1]
        with self.assertRaises(TypeError):
            max_integer(list_t)

if __name__ == '__main__':
    unittest.main()
