#!/usr/bin/python3
"""Defines is matrix function."""


def is_Matrix(matrix):
    """
    Check if the input is a valid matrix.

    Args:
        matrix: Object to be checked.

    Returns:
        bool: True if the input is a valid matrix, False otherwise.
    """

    if not isinstance(matrix, list) or not matrix:
        return False
    for row in matrix:
        if not isinstance(row, list):
            return False
        for element in row:
            if not isinstance(element, (int, float)):
                return False
    return True


"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divide each element in a matrix by a divisor.

    Args:
        matrix (list): A matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list: New matrix with elements rounded to two decimal places.

    Raises:
        TypeError: If the matrix is not a valid
        matrix or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """

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
