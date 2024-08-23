#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints elements in an int list that's reversed'''
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
