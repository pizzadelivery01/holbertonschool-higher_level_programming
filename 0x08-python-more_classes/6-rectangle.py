#!/usr/bin/python3

"""module: 1-rectangle"""


class Rectangle:
    """class: Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init: self, width, height"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter: width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter: height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method: area"""
        if self.__width and self.__height:
            return (self.__width * self.__height)

    def perimeter(self):
        """method: perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ print rectangle"""
        poundrec = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                poundrec += '#'
            if i is not self.__height - 1:
                poundrec += '\n'
        return poundrec

    def __repr__(self):
        """ literal string representation of rectangle"""
        repstr = ""
        row = self.__width
        column = self.__height
        if self.__width == 0 or self.__height == 0:
            return repstr
        else:
            repst = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
            return repst

    def __del__(self):
        """deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
