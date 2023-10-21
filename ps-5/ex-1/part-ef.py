import numpy as np
from scipy.integrate import quad

def integrand(z, a):
    c = a-1
    return (c / (c + z)**2) * np.exp((a - 1) * np.log(z / (c + z)) - z / (c + z))

def integrate_function(a):
    result, _ = quad(integrand, 0, 1, args=(a))
    return result

test_values = [3.0/2,3,6,10]
for test in test_values:
    print(integrate_function(test))