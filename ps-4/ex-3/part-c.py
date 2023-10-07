from scipy.integrate import quadrature
import numpy as np
from math import factorial, exp, sqrt
def H_iterative_vectorized_complete(n, x):
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return 2*x
    else:
        H_n_minus_2 = np.ones_like(x)
        H_n_minus_1 = 2*x
        for i in range(2, n+1):
            H_n = 2*x*H_n_minus_1 - 2*(i-1)*H_n_minus_2
            H_n_minus_2, H_n_minus_1 = H_n_minus_1, H_n
        return H_n

def psi_iterative_vectorized_complete(n, x):
    return np.exp(-x**2/2) * H_iterative_vectorized_complete(n, x) / sqrt(2**n * factorial(n) * sqrt(np.pi))

def uncertainty_integrand_vectorized_complete(x, n):
    return x**2 * abs(psi_iterative_vectorized_complete(n, x))**2

integral_value, _ = quadrature(uncertainty_integrand_vectorized_complete, -10, 10, args=(5,), maxiter=100)
uncertainty = sqrt(integral_value)

print(uncertainty)
