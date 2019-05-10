#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    n = 0
    for i in new_matrix:
        new_matrix[n] = list(map(lambda x: x ** 2, i))
        n += 1
    return new_matrix
