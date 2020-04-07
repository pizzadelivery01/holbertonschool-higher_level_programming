#!/usr/bin/python3
"""
finds a peak in unsorted list
"""


def find_peak(list_of_integers):
    """
    finds a peak in unsorted list
    """
    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return take_me_to_the_mountain_top(
            list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]


def take_me_to_the_mountain_top(new_list, first, last):
    """
    finds peak with recursion
    """

    if last - first < 2:
        return None
    half = (first + last) // 2
    if new_list[half] >= new_list[half - 1]\
       and new_list[half] >= new_list[half + 1]:
        return new_list[half]
    return take_me_to_the_mountain_top(
        new_list, first, half) or take_me_to_the_mountain_top(
            new_list, half, last)
