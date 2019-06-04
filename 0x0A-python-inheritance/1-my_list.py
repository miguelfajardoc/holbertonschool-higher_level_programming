#!/usr/bin/python3
""" Module that contains a class list"""


class MyList(list):
    """Class that defines a list
    """

    def print_sorted(self):
        """module that print a list sorted

        """
        sor = self[:]
        sor.sort()
        print(sor)
