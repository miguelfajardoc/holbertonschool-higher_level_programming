#!/usr/bin/python3
""" square square !

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that makes squares"""

    def __init__(self, size, x=0, y=0, id=None):
        """ the init of square """

        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """ the dictionary for square"""
        new_dict = {}
        new_dict = super().to_dictionary()
        new_dict["size"] = new_dict["width"]
        del new_dict["width"]
        del new_dict["height"]
        return new_dict

    @property
    def size(self):
        """ get the size """
        return (self.width)

    @size.setter
    def size(self, value):
        """ set the size """
        self.width = value
        self.height = value

    def __str__(self):
        """ put the string """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    def update(self, *args, **kwargs):
        """ the update square method """

        if len(args) > 2:
            args = list(args)
            args.insert(2, args[1])
        if not args:
            kwargs2 = kwargs.copy()
            for key, value in kwargs2.items():
                if key == "size":
                    kwargs["width"] = value
                    kwargs["height"] = value
                    del kwargs[key]

        super().update(*args, **kwargs)
