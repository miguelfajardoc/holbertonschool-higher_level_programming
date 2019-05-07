#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if n == 1:
        arg = "argument"
    else:
        arg = "arguments"
    if n == 0:
        print("{:d} {}.".format(n, arg))
    else:
        print("{:d} {}:".format(n, arg))
    for i in range(1, n + 1):
        print("{:d}: {}".format(i, argv[i]))
