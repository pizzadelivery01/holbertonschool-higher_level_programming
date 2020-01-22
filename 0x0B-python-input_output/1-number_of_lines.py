#!/usr/bin/python3
"""
prints number of lines
"""


def number_of_lines(filename=""):
    """prints number of lines"""
    lnum = 0
    with open(filename, 'r', encoding='utf8') as f:
        for i in f:
            lnum += 1
    return (lnum)
