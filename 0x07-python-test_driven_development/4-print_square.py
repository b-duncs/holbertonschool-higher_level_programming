#!/usr/bin/python3
"""
Write a function that prints a square with the character #.
    -size is the size length of the square
    -size must be an integer,
        otherwise raise a TypeError exception with the message
        "size must be an integer"
    -if size is less than 0,
        raise a ValueError exception with the message
        "size must be >= 0"
    -if size is a float and is less than 0,
        raise a TypeError exception with the message
        "size must be an integer"
    -You are not allowed to import any module
"""


def print_square(size):
    """Prints a Square with the Character '#'"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
