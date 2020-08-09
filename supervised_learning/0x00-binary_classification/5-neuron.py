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

    def forward_prop(self, X):
        """foward propagation"""
        i = np.matmul(self.__W, X) + self.__b
        self.__A = self.sigmoid_func(i)
        return self.__A

    def sigmoid_func(self, X):
        """sigmoid function"""
        return 1.0/(1.0 + np.exp(-X))

    def cost(self, Y, A):
        """Cost of Model using logistic regresion"""
        return -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)).mean()

    def evaluate(self, X, Y):
        """evaluates neuron predictions"""
        self.forward_prop(X)
        return np.round(self.__A).astype(int), self.cost(Y, self.__A)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """calculates one pass of gradient descent on the nueron"""
        self.__W = (self.__W - alpha * np.dot(X, (A - Y).T).T / X.shape[1])
        self.__b = self.__b - alpha * (A - Y).mean()
