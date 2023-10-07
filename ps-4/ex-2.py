import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the potential function
def V(x):
    return x**4

# Function to compute the integrand for the period
def integrand(x, a):
    return 1/np.sqrt(V(a) - V(x))

# Function to compute the period using Gaussian quadrature
def compute_period(a):
    # Integrate from a to 0
    result, _ = quad(integrand, a, 0, args=(a,))
    # Multiply by the factor outside the integral to get T
    T = 4 * np.sqrt(1/2) * result
    return T

# Calculate the period for amplitudes ranging from a = 0 to a = 2
amplitudes = np.linspace(0.01, 2, 100)  # We start from 0.01 to avoid division by zero
periods = [compute_period(a) for a in amplitudes]

# Plot the results
plt.figure(figsize=(10,6))
plt.plot(amplitudes, periods, label='Period vs Amplitude')
plt.xlabel('Amplitude (a)')
plt.ylabel('Period (T)')
plt.title('Period of the Oscillator vs Amplitude')
plt.legend()
plt.grid(True)
plt.show()
