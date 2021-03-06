#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2:
            for i in value:
                if type(i) is not int or i < 0:
                    raise TypeError("position must be a tuple of 2 positive\
 integers")
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size with a setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.position[1] is not 0:
                for j in range(self.position[1]):
                    print("")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
