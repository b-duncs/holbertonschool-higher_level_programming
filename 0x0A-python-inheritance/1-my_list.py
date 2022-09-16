#!/usr/bin/python3
"""
Write a class MyList that inherits from list:
    -You can assume that all the elements of the list will be of type int
    -You are not allowed to import any module
"""


class MyList(list):
    """Defines a List"""

    def print_sorted(self):
        """Prints the List with Ascending Sort"""
        print(sorted(self))
