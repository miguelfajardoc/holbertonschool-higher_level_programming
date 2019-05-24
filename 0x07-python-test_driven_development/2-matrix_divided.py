def matrix_divided(matrix, div):
    """function that divide the numbers of a matrix"""

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(error)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for j in range(len(matrix)):
        if type(matrix[j]) != list:
            raise TypeError(error)
    new_matrix = [row[:] for row in matrix]
    for j in range(len(matrix)):
        size = len(matrix[0])
        if len(matrix[j]) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix[j])):
            if type(matrix[j][i]) != int and type(matrix[j][i]) != float:
                raise TypeError(error)
            new_matrix[j][i] = round((new_matrix[j][i]) / div, 2)
    return(new_matrix)
