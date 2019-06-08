#!/usr/bin/python3#
"""module rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the init function of Rectangle"""

        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """display the rectangle with '#'"""
        for i in range(self.__height):
            print("#" * self.__width)

    def area(self):
        """the area of the rectangle"""
        return (self.width * self.height)

    @property
    def width(self):
        """ get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ get the width """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ get the width """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
