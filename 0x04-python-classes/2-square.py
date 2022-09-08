#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 1-square.py)
    -Private instance attribute: size
    -Instantiation with optional size: def __init__(self, size=0):
        -size must be an integer, otherwise raise a TypeError exception
        with the message size must be an integer
        -if size is less than 0, raise a ValueError exception
        with the message size must be >= 0
    -Public instance method: def area(self): that returns the current square area
    -You are not allowed to import any module
"""


class Square:
    """Class Square with Private Attribute Size"""
    def __init__(self, size=0):
        """Instantiation with Optional Size: def __init__(self, size=0)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """
        Public Instance Method:
        def area(self): returns the current square area
        """
        return self.__size * self.__size
