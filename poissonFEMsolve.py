import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from mesh import *
from assemble import *
from boundary import *
from utils import *

# specify the domain and the force field f
omega = (0, 1) # domain
d_bc = [(0, 1), (1, 1)] # list of tuples of Dirichlet BC, each tuple is (location, value)
f = lambda x: x * ( x + 3 ) * np.exp ( x ) # the source function

# specifying the number of elements to discretize the domain
n_e = 5
n_n = n_e + 1
x = createMesh(n_n, omega=omega)

# assemble the stiffness matrix and load vector
A = stiffnessAssembly(x)
F = loadAssembly(x, f)

# apply the Dirichlet boundary conditions
A_bc, F_bc = DirichletBC(x, A, F, d_bc)

# solve the linear system of equations
A_bc = sp.csr_matrix(A_bc) # casting the matrix into csr matrix to make it faster
U = sp.linalg.spsolve(A_bc, F_bc)

# plot the solution and compare with exact solution
x2 = np.linspace(0, 1, 101)
s = x2.shape[0]
u_exact = np.zeros((s, 1))
u_fem = np.zeros((s, 1))
for i in range(s):
    u_exact[i] = exact(x2[i])
    u_fem[i] = fem_soln(x, U, x2[i])
    
plt.figure()
plt.plot(x2, u_exact, '-')
plt.plot(x, U, '--o')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Solid line: Exact solution, Dashed line: FE solution')

plt.figure()
plt.title('Error plot')
plt.plot(x2, u_fem - u_exact)
plt.xlabel('x')
plt.ylabel('$U(x) -U_{fem}(x)$')
