#!/usr/bin/python3
"""
In this task, you will write unittests for the function def max_integer(list=[]):.
    -Your test file should be inside a folder tests
    -You have to use the unittest module
    -Your test file should be python files (extension: .py)
    -Your test file should be executed by using this command:
        python3 -m unittest tests.6-max_integer_test
    -All tests you make must be passable by the function below
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ismax(self):
        self.assertEqual(max_integer([5, 12, 2, -6]), 12)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([12]), 12)
        self.assertEqual(max_integer([12, 1, 2, -6]), 12)
        self.assertEqual(max_integer([5, 1, 2, 12]), 12)
        self.assertEqual(max_integer([-5, -12, -2, -6]), -2)

    def test_isint(self):
        self.assertIsInstance(max_integer([5, 7, 3, -1]), int)
        self.assertIs(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()
