#!/usr/bin/python3
"""Module that contain class square
   ###
   ###
"""


class Rectangle:
    """A Class that contain a rectangle
    Args:
        Width (int)
        height (int)
    """

    def __init__(self, width=0, height=0):
        """The init function"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ the setter of the witdth,
           just positive ints"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """the getter of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ the setter of the height,
           just positive ints"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """define the area of the square"""
        return (self.height * self.width)

    def perimeter(self):
        """define the perimeter of the square"""
        if self.height  == 0 or self.width == 0:
            return (0)
        return (self.height * 2 + 2 * self.width)
