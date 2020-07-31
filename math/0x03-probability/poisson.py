#!/usr/bin/env python3
"""Class constructor"""


class Poisson:
    """poisson class"""
    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, lambtha=1.):
        """Class init"""
        if data is None and isinstance(lambtha, (float, int)):
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = lambtha
        else:
            if not isinstance(data, int):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)
