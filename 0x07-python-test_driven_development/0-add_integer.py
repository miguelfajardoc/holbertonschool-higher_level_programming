#!/usr/bin/python3
def add_integer(a, b=98):
    """Addition function of integers"""
    z = [a, b]
    s = ['a', 'b']

    for i in range(2):
        if type(z[i]) is float and type(z[i]) is not int:
            z[i] = int(z[i])
        elif type(z[i]) is not int:
            raise TypeError("{} must be an integer".format(s[i]))
    return(z[0] + z[1])
