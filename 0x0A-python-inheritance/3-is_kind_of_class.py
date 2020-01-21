#!/usr/bin/python3
"""
has is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """ True if instance or inherited, or false"""
    return (isinstance(obj, a_class))
