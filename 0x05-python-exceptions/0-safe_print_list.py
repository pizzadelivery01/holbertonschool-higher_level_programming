#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    x = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            x++
        except IndexError:
        print("")
        return(x)
    print("")
    return(x)
