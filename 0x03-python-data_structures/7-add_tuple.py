#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    if len(tuple_a) >= 2:
        a = tuple_a
    elif len(tuple_a) == 1:
        a[0] = tuple_a[0]
    if len(tuple_b) >= 2:
        b = tuple_b
    elif len(tuple_b) == 1:
        b[0] = tuple_a[0]

    new_tuple = a[0] + b[0], a[1] + b[1]
    return(new_tuple)
