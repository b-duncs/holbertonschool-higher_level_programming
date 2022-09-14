#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
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
    -Public instance method: def area(self):
        that returns the rectangle area
    -Public instance method:
        def perimeter(self):
            that returns the rectangle perimeter:
                -if width or height is equal to 0,
                    perimeter has to be equal to 0
    -print() and str() should print the rectangle with the character #:
        -if width or height is equal to 0,
            return an empty string
    -repr() should return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
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

    def area(self):
        """Public Instance Method: def area(self)"""
        return self.__width * self.__height

    def perimeter(self):
        """Public Instance Method: def perimeter(self)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Public Instance Method: def __str__(self)"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for x in range(self.__height):
            [rectangle.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """Public Instance Method: def __repr__(self)"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle
