#!/usr/bin/python3
"""Write in a file"""


def write_file(filename="", text=""):
    """function that write in a file and return the number of chars written"""

    with open(filename, mode='w', encoding='utf-8') as a_file:
        written = a_file.write(text)

    return written
