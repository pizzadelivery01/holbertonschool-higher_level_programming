#!/usr/bin/python3
"""
BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """area and integer_validator"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """makes sure value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """a rectangle"""
    def __init__(self, width, height):
        """rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
