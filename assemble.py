import numpy as np
import scipy.sparse as sp
from basis import *

def loadAssembly(x, f):
    """Assemble and return the load vector
    for the 1D mesh x and force f""" 
    N = x.shape[0]
    F = np.zeros((N, 1))
    
    for i in range( N-1):
        F[i] = F[i] + intHat2(x[i], x[i+1], f)
        F[i+1] = F[i+1] + intHat1(x[i], x[i+1], f)
    return F


def stiffnessAssembly(x):
    """Assemble and return a sparse stiffness matrix  A
    for the given 1D mesh x""" 
    N = x.shape[0]
    h = x[1:]-x[0:-1] # get the element sizing
    
    # initiate a sparse A matrix and the first and last element of the diagonal
    A = sp.lil_matrix((N, N), dtype=np.float64)
    
    # loop through the diagonal to 
    for i in range(N-1):
        A[i,i] += 1/h[i]
        A[i,i+1] -= 1/h[i]
        A[i+1,i] -= 1/h[i]
        A[i+1,i+1] += 1/h[i]
    return A
    