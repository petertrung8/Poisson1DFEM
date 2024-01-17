import numpy as np
import copy


def DirichletBC(x, A, F, bc=[(0,0), (1, 0)]):
    """Apply the Dirichlet BC to the stiffness and load matrix and 
    return the new A, F"""
    n_bc = len(bc)
    
    # find the row and column that correspond to the boundary condition
    idx = [int(np.where(x==i[0])[0]) for i in bc]
    for i in range(n_bc):
        F = F - A[:, idx[i]]*bc[i][1]
        F[idx[i]] = bc[i][1]
    
    for i in range(n_bc):
        A[:, idx[i]] = 0
        A[idx[i], :] = 0
        A[idx[i], idx[i]] = 1
        
    return A, F
