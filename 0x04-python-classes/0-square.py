#!/usr/bin/python3
"""
Write a class Square that defines a square by:
    -Private instance attribute: size
    -Instantiation with size (no type/value verification)
    -You are not allowed to import any module
"""


class Square:
    """Class Square with Private Attribute Size"""
    def __init__(self, size):
        """Instantiation with Size (no type/value verification)"""
        self.__size = size
