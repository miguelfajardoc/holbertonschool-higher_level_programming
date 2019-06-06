#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
pascal = []
    for i in range(n):
        if len(pascal) < 2:
            add = 1
        else:
            add = 2
        print(pascal)
