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

    def to_dictionary(self):
        """ the dictionary for Rectangle """
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['width'] = self.width
        new_dict['height'] = self.height
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict

    def update(self, *args, **kwargs):
        """ the update rectangle method """
        for n in range(len(args)):
            if n == 0:
                Base.__init__(self, args[0])
            elif n == 1:
                self.width = args[n]
            elif n == 2:
                self.height = args[n]
            elif n == 3:
                self.x = args[n]
            else:
                self.y = args[n]

        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    Base.__init__(self, value)
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                else:
                    self.y = value

    def __str__(self):
        """ modificate the str method """
        return("[{}] ({:d}) {:d}/{:d} - {:d}/{:d}"
               .format(self.__class__.__name__, self.id, self.x, self.y,
                       self.width, self.height))

    def display(self):
        """display the rectangle with '#'"""
        for e in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

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
