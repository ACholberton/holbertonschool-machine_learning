#!/usr/bin/env python3
""" This funciton performs matrix multiplication """


def mat_mul(mat1, mat2):
    """using nested loops we iterate through
    both matrices in order to get their shapes and multiply"""

    new_matrix = []

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                new_matrix[i][j] += mat1[i][j] * mat2[i][j]

    return new_matrix
