#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Function replaces element in list without altering original'''
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    else:
        copy_list = my_list[:]
        copy_list[idx] = element
        return copy_list
