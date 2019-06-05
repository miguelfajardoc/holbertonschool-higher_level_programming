#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """function that append in a file and return the number of chars written"""

    with open(filename, mode='a', encoding='utf-8') as a_file:
        written = a_file.write(text)

    return written
