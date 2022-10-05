#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:
    -You must use the with statement
    -You don’t need to manage exceptions if the JSON string
        doesn’t represent an object.
    -You don’t need to manage file permissions / exceptions.
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode='r', encoding="utf-8") as myFile:
        return json.loads(myFile.read())
