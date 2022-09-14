#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
    -Private instance attribute: width:
        -property def width(self): to retrieve it
        -property setter def width(self, value): to set it:
            -width must be an integer,
                otherwise raise a TypeError exception with the message
                "width must be an integer"
            -if width is less than 0,
                raise a ValueError exception with the message
                "width must be >= 0"
    -Private instance attribute: height:
        -property def height(self): to retrieve it
        -property setter def height(self, value): to set it:
            -height must be an integer,
                otherwise raise a TypeError exception with the message
                "height must be an integer"
            -if height is less than 0,
                raise a ValueError exception with the message
                "height must be >= 0"
    -Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
    -You are not allowed to import any module
"""


class Rectangle:
    """Defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Instantiation with Optional Width and Height:
        def __init__(self, width=0, height=0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private Instance Attribute Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property Setter Width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private Instance Attribute Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property Setter Height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
