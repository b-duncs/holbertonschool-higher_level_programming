#!/usr/bin/python3
def no_c(my_string):
    for x in range(len(my_string)):
        x = "Cc"
        y = ""
        new_string = my_string.maketrans(x, y)
        return my_string.translate(new_string)
