#!/usr/bin/env python3
"""this funciton returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """Using nested loops to iterate through the rows and columns"""
    tp_matrix = []

    for rows in range(len(matrix)):
        for column in range(len(matrix[0])):
            tp_matrix = [matrix[rows][column]]

    return (tp_matrix)
