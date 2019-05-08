#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        n = 0
        for i in rows:
            print("{:d}".format(i), end="")
            n += 1
            if n < len(rows):
                print(" ", end="")
        print("")
