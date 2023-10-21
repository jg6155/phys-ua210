import numpy as np
import matplotlib.pyplot as plt
from part_b import time, signal, fit_signal
residuals = signal - fit_signal
std_residuals = np.std(residuals)
# Plot residuals
if __name__ == "__main__":
    plt.figure(figsize=(10, 6))
    plt.plot(time, residuals, 'o', label='Residuals', markersize=4)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Time(s)')
    plt.ylabel('Residual')
    plt.title('Residuals of the Third-order Polynomial Fit')
    plt.legend()
    plt.grid(True)
    plt.show()

