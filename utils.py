import numpy as np
from basis import *

def fem_soln(x, U, xp):
    """Return the interpolation of the FE results"""
    M = x.shape[0]
    for i in range(M-1):
        if xp >= x[i] and xp <=x [i+1]:
            return hat2(xp, x[i], x[i+1])*U[i]+hat1(xp, x[i], x[i+1])*U[i+1]

def exact(x):
    """Return the value of the exact solution of Poisson equation
    with a source f of f(x) = x * ( x + 3 ) * exp ( x )"""
    return x * ( 1 - x ) * np.exp ( x )+1
