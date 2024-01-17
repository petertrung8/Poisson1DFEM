import numpy as np
import copy


def DirichletBC(x, A, F, loc, bc):
    """Apply the Dirichlet BC to the stiffness and load matrix and 
    return the new A, F"""
    n_bc = len(bc)
    
    # find the row and column that correspond to the boundary condition
    idx = [int(np.where(x==i)[0]) for i in loc]
    for i in range(n_bc):
        F = F - A[:, idx[i]]*bc[i]
        F[idx[i]] = bc[i]
    
    for i in range(n_bc):
        A[:, idx[i]] = 0
        A[idx[i], :] = 0
        A[idx[i], idx[i]] = 1
        
    return A, F
