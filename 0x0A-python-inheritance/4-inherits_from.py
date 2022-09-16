#!/usr/bin/python3
"""
Write a function that returns True
    if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    -You are not allowed to import any module
"""


def inherits_from(obj, a_class):
    """Returns True if Object is an Instance of an Inherited Specified Class"""
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
