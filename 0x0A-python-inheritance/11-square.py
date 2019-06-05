#!/usr/bin/python3
""" Module that contains a class geometry"""


class BaseGeometry:
    """class geometryc

    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0". format(name))


class Rectangle(BaseGeometry):
    """class rectangle

    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return("[{}] {:d}/{:d}".format(self.__class__.__name__, self.__width,
                                       self.__height))

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    """class Square
    """
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.__size = size
