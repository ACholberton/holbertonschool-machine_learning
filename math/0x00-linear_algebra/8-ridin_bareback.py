#!/usr/bin/python3

def mat_mul(mat1, mat2):
    new_matrix = []

    if len(mat1) == len(mat2):
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    new_matrix[i][j] += mat1[i][j] * mat2[i][j]

    for m in new_matrix:
        return (m)
