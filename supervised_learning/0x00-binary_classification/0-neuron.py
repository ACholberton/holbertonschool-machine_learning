#!/usr/bin/env python3
""" Class neuron"""

import numpy as np


class Neuron:
    def __init__(self, nx):
        """Class init"""
        self.nx = nx

        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0