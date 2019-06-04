#!/usr/bin/python3
""" Module that contains a function"""


def inherits_from(obj, a_class):
    """module that check if an object is instance given class

    """
    if type(obj) == a_class:
        return(False)
    return issubclass(type(obj), a_class)
