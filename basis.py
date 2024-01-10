import numpy as np

### Basis function
def hat1(x, x1, x2):
    """Returns the value of first half of hat function at x"""
    y = (x-x1)/(x2-x1)
    return y

def hat2(x, x1, x2):
    """Returns the value of second half of hat function at x"""
    y = (x2-x)/(x2-x1)
    return y


### Definite integrals
def intHat1(x1, x2, f):
    """Return the definite integral of hat1 and f-function 
    from x1 to x2 using Simpson rule"""
    xm = (x1+x2)*0.5
    y = (x2-x1)*(f(x1)*hat1(x1,x1,x2) + 4*f(xm)*hat1(xm,x1,x2) +\
         f(x2)*hat1(x2,x1,x2))/6
    return y

def intHat2(x1, x2, f):
    """Return the definite integral of hat2 and f-function 
    from x1 to x2 using Simpson rule"""
    xm = (x1+x2)*0.5
    y = (x2-x1)*(f(x1)*hat2(x1,x1,x2) + 4*f(xm)*hat2(xm,x1,x2) +\
         f(x2)*hat2(x2,x1,x2))/6
    return y
