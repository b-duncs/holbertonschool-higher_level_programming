#!/usr/bin/python3
def no_c(my_string):
    for x in range(len(my_string)):
        if x != 'c' and x != 'C':
            return "".join(x)

