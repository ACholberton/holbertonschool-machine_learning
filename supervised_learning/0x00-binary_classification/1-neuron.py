#!/usr/bin/env python3
""" Class neuron"""
import numpy as np


class Neuron:
    """class init"""

    def __init__(self, nx):

        if type(nx) is not int:
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Return weights"""
        return self.__W

    @property
    def b(self):
        """return bias"""
        return self.__b

    @property
    def A(self):
        """return output"""
        return self.__A
