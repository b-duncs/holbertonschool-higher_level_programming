#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n:
    -Returns an empty list if n <= 0
    -You can assume n will be always an integer
    -You are not allowed to import any module
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
        the Pascal’s triangle of n"""
    list = []
    if n <= 0:
        return list
    last = [1]
    for row in range(n):
        new_list = []
        if row == 0:
            new_list = [1]
        else:
            for column in range(row + 1):
                if column == 0:
                    new_list.append(0 + last[column])
                elif column == (row):
                    new_list.append(last[column - 1] + 0)
                else:
                    new_list.append(last[column - 1] + last[column])
        last = new_list
        list.append(new_list)
    return list
