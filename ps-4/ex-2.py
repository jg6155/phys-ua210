import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def V(x):
    return x**4

def integrand(x, a):
    return 1/np.sqrt(V(a) - V(x))

def compute_period(a):
    result, _ = quad(integrand, a, 0, args=(a,))
    T = 4 * np.sqrt(1/2) * result
    return T

amplitudes = np.linspace(0.01, 2, 100)  
periods = [compute_period(a) for a in amplitudes]


plt.figure(figsize=(10,6))
plt.plot(amplitudes, periods, label='Period vs Amplitude')
plt.xlabel('Amplitude (a)')
plt.ylabel('Period (T)')
plt.title('Period of the Oscillator vs Amplitude')
plt.legend()
plt.grid(True)
plt.show()
