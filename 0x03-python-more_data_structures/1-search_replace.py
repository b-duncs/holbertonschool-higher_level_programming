#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list[:]
    for x in range(len(copy_list)):
        if copy_list[x] == search:
            copy_list[x] = replace
    return copy_list
