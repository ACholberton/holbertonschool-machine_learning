#!/usr/bin/env python3
""" This function calculates the shape of a matrix """


def matrix_shape(matrix):
    """I use try and except to append the shape values into a new list"""

    new_matrix = []

    try:
        new_matrix.append(len(matrix))
        new_matrix.append(len(matrix[0]))
        new_matrix.append(len(matrix[0][0]))
    except:
        pass
    return (new_matrix)
