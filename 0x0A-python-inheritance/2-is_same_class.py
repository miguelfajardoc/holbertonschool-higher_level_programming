#!/usr/bin/python3
""" Module that contains a function"""


def is_same_class(obj, a_class):
    """module that check if an object is exactly the same given class

    """
    if type(obj) == a_class:
        return True
    else:
        return False
