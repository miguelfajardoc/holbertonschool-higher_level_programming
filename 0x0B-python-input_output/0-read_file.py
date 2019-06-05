#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """function that read a file"""

    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
