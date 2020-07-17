#!usr/bin/env python3
"""This funciton calculates the shape of matrix"""


def matrix_shape(matrix):
    """Function to calculate the shape"""
    
    if not matrix:
        """check if matrix exists"""
        return None

    if type(matrix[0]) is not list:
        return[len(matrix)]
    return [len(matrix)] + matrix_shape(matrix[0])
