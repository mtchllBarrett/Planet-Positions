import numpy as np

def rad(theta):
    # converts `theta` from [DEG] to [RAD]
    return theta * np.pi / 180.

def deg(theta):
    # converts `theta` from [RAD] to [DEG]
    return theta * 180 / np.pi

def Kepler(E, e, M, deriv=False):
    
    # Kepler's equation
    # -----
    # E: eccentric anomaly
    # e: eccentricity of the orbit
    # M: mean anomaly
    # -----
    # input values in [DEG]
    # -----
    # includes `deriv` option, set to `True` for the derivative of Kepler's eqn with respect to E
    
    if deriv:
        return 1 - e * np.cos(rad(E))
    else:
        return rad(E) - e * np.sin(rad(E)) - rad(M)
    
def Newton(x, f, df, desired_err = 1e-9):
    
    # Newton's method for finding roots of complicated equations
    # -----
    # x: free parameter
    # f: function to solve
    # df: derivative of f
    # desired_err: the function will try to get "close enough" to the root in question;
    #              desired_err is how close you deem close enough.
    #              for these calculations, 1e-9 is a pretty reasonable value
    # -----
    
    err = desired_err + 1
    xi = x
    
    while err > desired_err:
        xf = xi - f(xi) / df(xi)
        err = abs(xf - xi)
        xi = xf
        
    return xf

def get_f(E, e):
    coef = np.sqrt((1+e) / (1-e))
    theta = rad(E / 2)
    return deg(2 * np.arctan(coef * np.tan(theta))) % 360

def get_l(f, w):
    return (f + w) % 360

def get_r(a, e, E):
    return a * (1 - e * np.cos( rad(E) ))