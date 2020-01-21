#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """subclass"""
    def __init__(self):
        """init obj"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
