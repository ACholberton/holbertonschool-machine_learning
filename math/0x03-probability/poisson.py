#!/usr/bin/env python3
"""Class constructor"""


class Poisson:
    """poisson class"""

    def __init__(self, data=None, lambtha=1.):
        """Class init"""

        self.e = 2.7182818285
        self.pi = 3.1415926536

        if data is None and isinstance(lambtha, (float, int)):
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = lambtha
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)
