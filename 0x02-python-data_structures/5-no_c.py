#!/usr/bin/python3
def no_c(my_string):
    remove = {67: None, 99: None}
    new_string = my_string.translate(remove)
    return new_string
