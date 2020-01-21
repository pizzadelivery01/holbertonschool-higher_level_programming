#!/usr/bin/python3
"""
module has function is_same_class
"""


def is_same_class(obj, a_class):
    """returns true if exact class as a_class or false"""
    return (type(obj) == a_class)
