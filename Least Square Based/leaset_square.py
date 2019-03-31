import numpy as np
from itertools import product


class LSM:
    def __init__(self, func=None, l2=False, l2_lambda=1):
        self.func = func
        self.func_list = self._gen_func_list(func)
        self.l2 = l2
        self.l2_lambda = l2_lambda

    def _gen_func_list(self, func):
        if func is None:
            return [np.vectorize(lambda x:x)]
        elif func == "poly":
            return [self._gen_poly(i) for i in range(1, 11)]
        else:
            raise Exception

    def _gen_poly(self, i):
        return np.vectorize(lambda x:np.power(x, i))
