import numpy as np
import matplotlib.pyplot as plt
from part_a import time, signal
time_scaled = (time - np.mean(time)) / np.std(time)

# Construct the design matrix for a third-order polynomial
A = np.vstack([np.ones_like(time_scaled), time_scaled, time_scaled**2, time_scaled**3]).T

# Apply SVD
U, s, Vt = np.linalg.svd(A, full_matrices=False)
c = U.T @ signal
w = np.linalg.inv(np.diag(s)) @ c
coefficients = Vt.T @ w

# Construct the third-order polynomial using the obtained coefficients
fit_signal = A @ coefficients

# Plot the original data and the fitted polynomial
if __name__ == "__main__":
    plt.figure(figsize=(10, 6))
    plt.plot(time, signal, 'o', label='Signal Data', markersize=4)
    plt.plot(time, fit_signal, 'o',markersize = 2, label='Third-order Polynomial Fit', linewidth=1)
    plt.xlabel('Time(s)')
    plt.ylabel('Signal')
    plt.title('Third-order Polynomial Fit')
    plt.legend()
    plt.grid(True)
    plt.show()