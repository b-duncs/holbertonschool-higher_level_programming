#!/usr/bin/python3
def no_c(my_string):
    remove = {'C': None, 'c': None}
    new_string = my_string.translate(remove)
    return new_string
