#!/usr/bin/python3
"""Number of lines in a file"""


def read_lines(filename="", nb_lines=0):
    """function that count the lines of a file and print it"""
    lines = 0
    with open(filename, encoding='utf-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            for line in a_file:
                if lines == nb_lines:
                    break
                print(line, end="")
                lines += 1

    return lines
