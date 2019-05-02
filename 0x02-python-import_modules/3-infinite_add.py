#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    s = 0
    for i in range(1, n):
        s = s + int(argv[i])
    print(s)
