#!/usr/bin/python3
def text_indentation(text):
    """a function that puts \n in every '.', '?', and ':'"""

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i - 1] == '.' or text[i - 1] == ':' or text[i - 1] == '?':
            print("\n")
            if text[i] != " ":
                print(text[i], end="")
        else:
            print(text[i], end="")
