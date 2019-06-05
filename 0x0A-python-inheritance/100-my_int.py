#!/usr/bin/python3
"""this comdule contains a strange int class"""


class MyInt(int):
    """this is an rebel int"""

    def __ne__(self, other):
        if isinstance(other, int):
            return super().__eq__(other)
        return False


    def __eq__(self, other):
        if isinstance(other, int):
            return super().__ne__(other)
        return True
