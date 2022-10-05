#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:
    -You must use the with statement
    -You don’t need to manage file permission or file doesn't exist exceptions.
    -You are not allowed to import any module
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode='r') as myFile:
        print(myFile.read(), end="")
