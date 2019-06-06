#!/usr/bin/python3
"""JSON Class"""


class Student:
    """Class student json"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if type(attrs) == list:
            for atribute in attrs:
                if type(atribute) != str:
                    return self.__dict__
                dictionary = {}
                for key in self.__dict__:
                    for atribute in attrs:
                        if key == atribute:
                            dictionary[key] = self.__dict__[key]
                return dictionary
