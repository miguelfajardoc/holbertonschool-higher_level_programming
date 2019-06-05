#!/usr/bin/python3
"""this comdule contains a strange int class"""


class MyInt(int):
    """this is an rebel int"""

    def __ne__(self, other):
        return super().__eq__(other)


    def __eq__(self, other):
        return super().__ne__(other)
