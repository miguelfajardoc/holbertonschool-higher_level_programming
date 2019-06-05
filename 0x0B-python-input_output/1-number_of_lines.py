#!/usr/bin/python3
"""Number of lines in a file"""


def number_of_lines(filename=""):
    """function that count the lines of a file"""
    lines = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            lines += 1
    return lines
