#!/usr/bin/python3
def max_integer(my_list=[]):
        my_list.sort()
        return('Max: {:d}'.format(my_list[-1]))