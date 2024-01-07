#!/usr/bin/python3

def is_Matrix(matrix):
    if not isinstance(matrix, list) or not matrix:
        return False
    for row in matrix:
        if not isinstance(row, list):
            return False
        for element in row:
            if not isinstance(element, (int, float)):
                return False
    return True


def matrix_divided(matrix, div):
    new_matrix = []

    if is_Matrix(matrix) is False:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append((new_row))
    return new_matrix
