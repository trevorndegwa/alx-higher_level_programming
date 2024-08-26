#!/usr/bin/python3
def best_score(a_dictionary):
    '''Returns key with biggest int value'''
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
