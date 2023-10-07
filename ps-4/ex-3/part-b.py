from math import factorial, exp, sqrt
import matplotlib.pyplot as plt
import numpy as np
def H_iterative(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    else:
        H_n_minus_2 = 1
        H_n_minus_1 = 2*x
        for i in range(2, n+1):
            H_n = 2*x*H_n_minus_1 - 2*(i-1)*H_n_minus_2
            H_n_minus_2, H_n_minus_1 = H_n_minus_1, H_n
        return H_n


def psi_iterative(n, x):
    return exp(-x**2/2) * H_iterative(n, x) / sqrt(2**n * factorial(n) * sqrt(np.pi))


x_values_30 = np.linspace(-10, 10, 400)
y_values_30 = [psi_iterative(30, x) for x in x_values_30]

plt.figure(figsize=(10, 6))
plt.plot(x_values_30, y_values_30, label=f"n = 30")
plt.title("Harmonic Oscillator Wavefunction for n = 30")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend()
plt.grid(True)
plt.show()
