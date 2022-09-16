#!/usr/bin/python3
"""
Write a function that returns the list of available attributes and methods of an object:
    -Returns a list object
    -You are not allowed to import any module
"""


def lookup(obj):
    """Returns a List Object"""
    return dir(obj)
