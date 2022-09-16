#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    -Instantiation with width and height:
        def __init__(self, width, height)::
        -width and height must be private
        -width and height must be positive integers,
            validated by integer_validator
    -the area() method must be implemented
    -print() should print, and str() should return,
        the following rectangle description: [Rectangle] <width>/<height>
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

    def area(self):
        """Public Instance Area"""
        return self.__width * self.__height

    def __str__(self):
        """Public Instance"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
