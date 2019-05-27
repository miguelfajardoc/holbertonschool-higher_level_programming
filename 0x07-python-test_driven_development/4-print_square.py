#!/usr/bin/python3
""" module that print square
"""


def print_square(size):
    """Function that print a square of size with #

       Args:
       size: (positive int) the size of the square
    """
    if isinstance(size, (int)) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
