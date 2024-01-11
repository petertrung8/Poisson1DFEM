Linear FEM Solver for 1D Poisson's Equation
==============
# Overview

This repository contains a Python implementation of a linear finite element method (FEM) solver for the Poisson's equation in 1D on a finite interval with Dirichlet boundary conditions.

The problem solved in the script is as follows:
```math
- u'' = f(x), 0<x<1
```
where
```math
f(x) =  x * ( x + 3 ) * e^ x
```
and 
```math
u(0) = u(1) = 1
```

# Key Features
Solves the Poisson equation with a given source term and boundary conditions, source term and boundary conditions can be modified.
Performs a convergence analysis to assess the accuracy of the solution.

# Files
* **poissonFEMsolve.py**: Main script for solving the Poisson equation.
* **mesh_convergence.py**: Script for performing convergence analysis on different meshes.
* **assemble.py**: Functions for assembling the stiffness and load matrices.
* **basis.py**: Functions for defining the basis functions.
* **boundary.py**: Functions for applying boundary conditions (currently only Dirichlet BC).
* **mesh.py**: Functions for discretization of the domain (equidistant or random nodes). 
* **utils.py**: Utility functions such as exact solution and point interpolation.

# Usage
1. Solve the Poisson equation:
* Run python **poissonFEMsolve.py** to solve the equation with the default parameters.
* Customize parameters as needed within the script, mainly the variables `omega` (domain bounds), `d_bc` (Dirichlet BC), `f` (source function) and `n_e` (number of elements).
![Solution of the FEM solver compared with the exact solution](/figures/fem_solution.png)
![Error of the FEM solver compared with the exact solution](/figures/fem_error.png)
2. Perform convergence analysis:
* Run python **mesh_convergence.py** to analyze the convergence behavior for different mesh sizes.
* Current mesh sizing evaluated are 10, 50, 100, 500, 1000 elements
![L2-error of the different meshes with exact solution](/figures/L2-error.png)

* With increasing elements, the L2-norm error decreases and converges
* From the graph, 100 elements could be enough to model the solution accurately as it is the convergence point
# Dependencies

Python 3.x

NumPy

Matplotlib

Scipy

# Author

Peter Mai


# References

Larson, M.G. and Bengzon, F., 2013. The finite element method: theory, implementation, and applications (Vol. 10). Springer Science & Business Media.

Li, Z., Qiao, Z. and Tang, T., 2017. Numerical solution of differential equations: introduction to finite difference and finite element methods. Cambridge University Press.