#!/usr/bin/python3
"""This funciton adds 2 arrays """

def add_arrays(arr1, arr2):

    NL = []
    if len(arr1) == len(arr2):
        """Checks if both arrays have the same length"""
        NL = [arr1[row] + arr2[row] for row in range(len(arr1))]
        return NL
    else:
        return None
