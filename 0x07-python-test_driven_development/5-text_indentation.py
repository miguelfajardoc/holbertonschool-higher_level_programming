#!/usr/bin/python3
"""Module to indent text
"""


def text_indentation(text):
    """a function that puts \n in every '.', '?', and ':'

    Args:
        text (str): the string to indent
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i - 1] == '.' or text[i - 1] == ':' or text[i - 1] == '?':
            print("\n")
            if text[i] != " ":
                print(text[i], end="")
        else:
            print(text[i], end="")
