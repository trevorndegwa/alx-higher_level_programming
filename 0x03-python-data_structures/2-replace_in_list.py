#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''Replaces element at index idx in list'''
    if (idx < 0) or (idx >= len(my_list)):
        return (my_list)
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
        return (my_list)
