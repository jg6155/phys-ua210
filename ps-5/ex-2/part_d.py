import numpy as np
import matplotlib.pyplot as plt
from part_b import signal, time, fit_signal, time_scaled

residuals = signal - fit_signal
# Define a function to fit polynomial and return residuals and condition number
def fit_polynomial(time_scaled, signal, order):
    # Construct the design matrix for the given order polynomial
    A_high = np.vstack([time_scaled**i for i in range(order+1)]).T
    
    # Calculate the condition number
    condition_number = np.linalg.cond(A_high)
    
    # Apply SVD
    U, s, Vt = np.linalg.svd(A_high, full_matrices=False)
    c = U.T @ signal
    w = np.linalg.inv(np.diag(s)) @ c
    coefficients_high = Vt.T @ w
    
    # Construct the polynomial using the obtained coefficients
    fit_signal_high = A_high @ coefficients_high
    
    # Calculate residuals
    residuals_high = signal - fit_signal_high
    
    return residuals_high, condition_number, fit_signal_high

# Fit a 10th order polynomial as an example of a higher-order polynomial
order = 10
residuals_high, condition_number, fit_signal_high = fit_polynomial(time_scaled, signal, order)
if __name__ == "__main__":
    # Plot the original data and the fitted polynomial
    plt.figure(figsize=(10, 6))
    plt.plot(time, signal, 'o', label='Signal Data', markersize=4)
    plt.plot(time, fit_signal_high, 'o', label=f'{order}-order Polynomial Fit', linewidth=1)
    plt.xlabel('Time(s)')
    plt.ylabel('Signal')
    plt.title(f'{order}-order Polynomial Fit')
    plt.legend()
    plt.grid(True)
    plt.show()

