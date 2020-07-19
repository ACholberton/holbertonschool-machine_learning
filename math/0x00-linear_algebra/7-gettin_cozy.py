#!usr/bin/env python3
""" This function concatenates 2 matrices along a specific axis """


def cat_matrices2D(mat1, mat2, axis=0):

    new_matrix = []

    if axis is 1:
        for i in range(len(new_matrix)):
            new_matrix[i].append(mat2[i][0])
    else:
        new_matrix = mat1 + mat2

    return new_matrix
