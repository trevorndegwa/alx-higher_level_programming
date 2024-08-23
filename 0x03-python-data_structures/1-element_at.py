#!/usr/bin/python3
def element_at(my_list, idx):
    '''Print element at index idx in list'''
    length = len(my_list)
    if (idx < 0) or (idx >= length):
        return None
    return (my_list[idx])
