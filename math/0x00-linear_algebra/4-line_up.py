#!/usr/bin/env python3
"""This funciton adds 2 arrays """


def add_arrays(arr1, arr2):

    NL = []
    if len(arr1) == len(arr2):
        """Checks if both arrays have the same length"""
        return None

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            NL.append(arr1[i] + arr2[2])

    return NL
