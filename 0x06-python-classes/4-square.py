#!/usr/bin/python3
"""Square class"""


class Square:
    """a square"""
    def __init__(self, size=0):
        """initializes the square"""
        self.size = size

    def area(self):
        """calculates the area of square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
