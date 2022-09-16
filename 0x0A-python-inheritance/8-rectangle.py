#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    -Instantiation with width and height: def __init__(self, width, height):
        -width and height must be private. No getter or setter
        -width and height must be positive integers, validated by integer_validator
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited Class Rectangle"""

    def __init__(self, width, height):
        """Public Instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
