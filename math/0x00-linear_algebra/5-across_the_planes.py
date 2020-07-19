#!/usr/bin/env python3
"""adds two matrices together"""

def add_matrices2D(mat1, mat2):
    """ This funciton adds 2 matrices together"""

    if len(mat1) == len(mat2) or len(mat1[0]) == len(mat2[0]):
        return None

    new_matrix = mat1[:]

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            new_matrix = [mat1[i][j] + mat2[i][j]]
        
    return new_matrix
