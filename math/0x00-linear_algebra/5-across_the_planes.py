#!/usr/bin/python3
"""adds tow matrices together"""

def add_matrices2D(mat1, mat2):

    new_matrix = []

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
                new_matrix = [mat1[i][j] + mat2[i][j]]
            else:
                return None
