#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    -You are not allowed to import any module
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if Object is an Instance of
    Specified Class or Inherited Class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
