#!/usr/bin/python3
def max_integer(my_list=[]):
        my_list.sort()
        return('{:d}'.format(my_list[-1]) if my_list else None)
