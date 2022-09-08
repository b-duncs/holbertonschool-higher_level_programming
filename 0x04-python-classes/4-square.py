#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 3-square.py)
    -Private instance attribute: size:
        -property def size(self): to retrieve it
        -property setter def size(self, value): to set it:
            -size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
            -if size is less than 0, raise a ValueError exception
            with the message size must be >= 0
    -Instantiation with optional size: def __init__(self, size=0):
    -Public instance method: def area(self):
        that returns the current square area
    -Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
        -if size is equal to 0, print an empty line
    -You are not allowed to import any module
"""


class Square:
    """Class Square with Private Attribute Size"""
    def __init__(self, size=0):
        """Instantiation with Optional Size: def __init__(self, size=0)"""
        self.size = size

    def area(self):
        """
        Public Instance Method:
        def area(self): returns the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter def size(self, value): to set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Public Instance Method:
        def my_print(self): prints in stdout the square with the character #
        """
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
