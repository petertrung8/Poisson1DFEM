import numpy as np


def createMesh(n, omega=(0, 1)):
    """Return an array of n nodes that are 
    equally spaced in the domain omega"""
    return np.linspace(omega[0], omega[1], n)


def createRandMesh(n, omega=(0, 1)):
    """Return an array of n nodes that are 
    randomly spaced in the domain omega"""
    x = np.random.uniform(low=omega[0], high=omega[1], size=(n-2,))
    return np.sort(np.append(x, np.array(omega)))
