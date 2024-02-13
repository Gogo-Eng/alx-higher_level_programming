#!/usr/bin/python3
"""
 function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix

    Args:
        matrix: the matrix to be divided through
        div: the divider

    Raises:
        TypeError:matrix must be a matrix (list of lists)\
                        of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        returns a new matrix
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(i, list) for i in matrix) or
            not all(isinstance(j, (int, float)) for i in matrix for j in i)):
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    row_length = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_result = []
    for row in matrix:
        column = []
        for element in row:
            column.append(round(element / div, 2))
        div_result.append(column)
    return div_result
