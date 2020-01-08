#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    m = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            m = m + 1
    except IndexError:
            print("")
            return(m)
    print("")
    return(m)
