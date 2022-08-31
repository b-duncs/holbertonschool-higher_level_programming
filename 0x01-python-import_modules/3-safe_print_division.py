#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except b is 0:
        result = "None"
        print("Inside result: {}".format(result))
    finally:
        print("{} / {} = {}".format(a, b, result))
