#!/usr/bin/python3
for i in range(99):
    if i != 98:
        print("{:0<2d}, ".format(i), end="")
    else:
        print("{:0<2d}".format(i))
