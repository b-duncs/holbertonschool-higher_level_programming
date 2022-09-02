#!/usr/bin/python3
def no_c(my_string):
    remove = {'C': None, 'c': None}
    print(my_string.translate(remove))
