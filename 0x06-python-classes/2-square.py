#!/usr/bin/python3
"""Square class making square"""


class Square:
    """Square class making square"""
    def __init__(self, size=0):
        """initializing Square class making square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
