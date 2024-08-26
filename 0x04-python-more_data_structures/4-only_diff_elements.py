#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''Returns set of all elements present in only 1 set'''
    return (set_1 ^ set_2)
