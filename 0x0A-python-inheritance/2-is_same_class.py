#!/usr/bin/python3
"""
Write a function that returns True
    if the object is exactly an instance of the specified class;
    otherwise False.
    -You are not allowed to import any module
"""


def is_same_class(obj, a_class):
    """Returns True if Object is an Instance of Specified Class"""
    if type(obj) == a_class:
        return True
    else:
        return False
