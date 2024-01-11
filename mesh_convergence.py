import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from mesh import *
from assemble import *
from boundary import *
from utils import *

# specify the domain and the force field f
omega = (0, 1)
d_bc = [(0, 0), (1, 0)]
f = lambda x: 1

# specifying the number of elements to discretize the domain
n_e = np.array([10, 50, 100, 500, 1000]) # five meshes to assess the mesh convergence
n_n = n_e + 1

# solve the Poisson equation for each mesh
x_s = np.linspace(0, 1, 1000)
mesh_conv = np.zeros((x_s.shape[0], n_n.shape[0])) # allocate memory
t = []
for i in range(len(n_n)):
    # discretize the domain using a mesh with same sized elements
    x = createRandMesh(n_n[i], omega=omega)

    # assemble the stiffness matrix and load vector
    A = stiffnessAssembly(x)
    F = loadAssembly(x, f)

    # apply the Dirichlet boundary conditions
    A_bc, F_bc = DirichletBC(x, A, F, d_bc)

    # solve the linear system of equations
    A_bc = sp.csr_matrix(A_bc) # casting the matrix into csr matrix to make it faster
    U = sp.linalg.spsolve(A_bc, F_bc)
    
    # interpolate the results so each mesh has same number of points
    for j in range(x_s.shape[0]):
        mesh_conv[j, i] = fem_soln(x, U, x_s[j])

# calculate the mean and max difference of u for each mesh to the previous one
exact_sol = exact(x_s)
conv_diff = mesh_conv.T-exact_sol
L2_err = np.linalg.norm(conv_diff, axis=1)

# plot the results of the convergence study
plt.figure()
plt.plot(n_e, L2_err, '-o')
plt.xscale('log')
plt.xlabel('Mesh size')
plt.ylabel('$||u_{fem} - u_{exact}||_{L2}$')
plt.title('L2-error of the different meshes with exact solution')

