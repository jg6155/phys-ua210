import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, e
from math import pi, sqrt

def calc_Madelung1(lattice_size):
    L = lattice_size
    res = 0
    for i in range(-L, L):
        for j in range(-L, L):
            for k in range(-L, L):
                if 0 == i == k == j:
                    continue
                if (i + j + k) % 2 == 1:
                    res += 1 / (sqrt(i**2 + j**2 + k**2))
                else:
                    res -= 1 / (sqrt(i**2 + j**2 + k**2))
    return res

def calc_Madelung2(lattice_size):
    L = lattice_size
    i, j, k = np.meshgrid(np.arange(-L, L), np.arange(-L, L), np.arange(-L, L), indexing='ij')
    distances = np.sqrt(i**2 + j**2 + k**2)
    distances[distances == 0] = np.inf
    sum_vals = np.where((i + j + k) % 2 == 0, 1, -1) / distances
    return np.sum(sum_vals)

def visualize_pattern():
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    for _ in range(100):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask]**2 + (X[mask] + 1j * Y[mask])
    plt.imshow(np.abs(Z) < 2, extent=(-2, 2, -2, 2), origin='lower', cmap='gray')
    plt.xlabel('X (real)')
    plt.ylabel('Y (imaginary)')
    plt.show()

def quadratic_formula(a, b, c):
    a, b, c = np.float64(a), np.float64(b), np.float64(c)
    root_1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
    root_2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
    if root_1 != root_2:
        return root_1, root_2
    return root_1

def quadratic_formula2(a, b, c):
    a, b, c = np.float64(a), np.float64(b), np.float64(c)
    root_1 = 2 * c / (-b + np.sqrt(b**2 - 4*a*c))
    root_2 = 2 * c / (-b - np.sqrt(b**2 - 4*a*c))
    if root_1 != root_2:
        return root_1, root_2
    return root_1

def main():
    # Test the quadratic formula functions
    print(quadratic_formula(0.001, 1000, 0.001))
    print(quadratic_formula2(0.001, 1000, 0.001))
    # Visualize the pattern
    visualize_pattern()

if __name__ == "__main__":
    main()
