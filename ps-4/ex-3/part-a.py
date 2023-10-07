from math import factorial, exp, sqrt
import matplotlib.pyplot as plt
import numpy as np

# Define the Hermite polynomial function using recursion
def H(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    else:
        return 2*x*H(n-1, x) - 2*(n-1)*H(n-2, x)

# Define the wavefunction for the harmonic oscillator
def psi(n, x):
    return exp(-x**2/2) * H(n, x) / sqrt(2**n * factorial(n) * sqrt(np.pi))

# Plot the wavefunctions for n = 0, 1, 2, and 3
x_values = np.linspace(-4, 4, 400)
for n in [0, 1, 2, 3]:
    y_values = [psi(n, x) for x in x_values]
    plt.plot(x_values, y_values, label=f"n = {n}")

plt.title("Harmonic Oscillator Wavefunctions for n = 0, 1, 2, and 3")
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend()
plt.grid(True)
plt.show()
