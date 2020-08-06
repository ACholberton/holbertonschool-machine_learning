#!/usr/bin/env python3
""" Class neuron"""

import numpy as np


class Neuron:
    def __init__(self, nx):
        """class init"""
        self.nx = nx

        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self._W = np.random.normal(size=(1, nx))
        self._b = 0
        self._A = 0

        @property
        def W(self):
            """Return weights"""
            return self._W
            
        @property
        def b(self):
            """Returns bias"""
            return self._b

        @property
        def A(self):
            """Return output"""
            return self._A
