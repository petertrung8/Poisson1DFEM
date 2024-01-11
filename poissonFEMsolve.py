import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from mesh import *
from assemble import *
from boundary import *

# specify the domain and the force field f
omega = (0, 1)
d_bc = [(0, 0), (1, 0)]
f = lambda x: x * ( x + 3 ) * np.exp ( x )

# specifying the number of elements to discretize the domain
n_e = 100
n_n = n_e + 1

x = createMesh(n_n, omega=omega)

# assemble the stiffness matrix and load vector
A = stiffnessAssembly(x)
F = loadAssembly(x, f)

# apply the Dirichlet boundary conditions
A_bc, F_bc = DirichletHomBC(x, A, F, d_bc)

# solve the linear system of equations
U = sp.linalg.spsolve(A_bc, F_bc)

# plot the solution
x2 = np.arange(0, 1.05, 0.05)
# plt.plot(x2, x2*(1-x2)/2, '-')
plt.plot(x2, x2 * ( 1 - x2 ) * np.exp ( x2 ), '-')
plt.plot(x, U, '--o')
