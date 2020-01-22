#!/usr/bin/python3
"""
appends string and returns num of chars added
"""


def append_write(filename="", text=""):
    """appends string and returns num of chars added"""
    with open(filename, 'a', encoding='UTF8') as f:
        s = str(text)
        f.write(s)
    return len(s)
