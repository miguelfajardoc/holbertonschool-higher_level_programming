#!/usr/bin/python3
j = 25
p = 1
may = 32
for i in range(97, 123):
    if p % 2 == 0:
        may = 32
    else:
        may = 0
    print("{}".format(chr(i + j - may)), end="")
    j = j - 2
    p = p + 1
