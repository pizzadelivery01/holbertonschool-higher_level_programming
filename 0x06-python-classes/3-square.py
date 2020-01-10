#!/usr/bin/python3
"""Square class defined"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initializes the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """defines area of square"""
        return (self.__size) ** 2
