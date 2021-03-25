from numba import vectorize
import numpy as n


@vectorize(['float64(float64)'], target='cuda')
def foo(x):
    return 1


foo(n.ones(1))
