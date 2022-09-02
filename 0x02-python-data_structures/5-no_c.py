#!/usr/bin/python3
def no_c(my_string):
    for x in range(len(my_string)):
        new_string = {'C': None, 'c': None}
        return my_string.translate(new_string)
