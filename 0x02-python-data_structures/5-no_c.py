#!/usr/bin/python3
def no_c(my_string):
    new_string = {'C': None, 'c': None}
    return my_string.translate(new_string)
