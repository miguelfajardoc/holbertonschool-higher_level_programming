#!/usr/bin/python3
""" The base module"""
import json
import os.path

class Base:
    """ The base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def load_from_file(cls):
        """ load from a file """
        name = cls.__name__ + ".json"
        lists = []
        if os.path.exists(name):
            with open(name, encoding='utf-8') as fil:
                lists = Base.from_json_string(fil.read())
                new = []
                for l in lists:
                    if type(l) is dict:
                        new.append(cls.create(**l))
                    else:
                        new.append(l)
                return new
        else:
            return lists

    @classmethod
    def create(cls, **dictionary):
        """ create a new thing"""
        args = []
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(*args, **dictionary)
        return dummy

    @staticmethod
    def from_json_string(json_string):
        """ bring the list representation of a json string"""
        if json_string is None or len(json_string) == 0:
            return([])
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json representation of a dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method to save a json in a file """
        new_list = []
        file_cls = cls.__name__ + ".json"
        with open(file_cls, mode='w', encoding='utf-8') as a_file:
            if list_objs is None:
                pass
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
            a_file.write(Base.to_json_string(new_list))
