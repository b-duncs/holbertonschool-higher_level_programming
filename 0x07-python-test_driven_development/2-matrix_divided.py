#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
    -matrix must be a list of lists of integers or floats,
        otherwise raise a TypeError exception with the message
        "matrix must be a matrix (list of lists) of integers/floats"
    -Each row of the matrix must be of the same size,
        otherwise raise a TypeError exception with the message
        "Each row of the matrix must have the same size"
    -div must be a number (integer or float),
        otherwise raise a TypeError exception with the message
        "div must be a number"
    -div can’t be equal to 0,
        otherwise raise a ZeroDivisionError exception with the message
        "division by zero"
    -All elements of the matrix should be divided by div,
        rounded to 2 decimal places
    -Returns a new matrix
    -You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """Divides All Elements of a Matrix"""
    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
