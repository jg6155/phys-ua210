import matplotlib.pyplot as plt
import numpy as np
from part_b import time, signal, time_scaled
# Define the maximum harmonic to consider
max_harmonic = 10
period = (time[-1] - time[0]) / 2  # Period equal to half of the time span
frequencies = [1/period * (i+1) for i in range(max_harmonic)]

# Construct the design matrix for the sin and cos functions
A_harmonic = np.column_stack([np.ones(time_scaled.shape)] + [np.sin(2 * np.pi * f * time) for f in frequencies] + [np.cos(2 * np.pi * f * time) for f in frequencies])

# Apply SVD
U, s, Vt = np.linalg.svd(A_harmonic, full_matrices=False)
c = U.T @ signal
w = np.linalg.inv(np.diag(s)) @ c
coefficients_harmonic = Vt.T @ w

# Construct the signal using the obtained coefficients
fit_signal_harmonic = A_harmonic @ coefficients_harmonic

# Calculate residuals
residuals_harmonic = signal - fit_signal_harmonic
std_residuals_harmonic = np.std(residuals_harmonic)

# Compute the Fast Fourier Transform (FFT) of the signal
fft_values = np.fft.fft(signal)
frequencies_fft = np.fft.fftfreq(len(time), d=np.mean(np.diff(time)))

# Only consider positive frequencies
positive_freq_indices = np.where(frequencies_fft > 0)
fft_values_positive = fft_values[positive_freq_indices]
frequencies_positive = frequencies_fft[positive_freq_indices]

# Identify dominant frequency
dominant_frequency = frequencies_positive[np.argmax(np.abs(fft_values_positive))]
dominant_period = 1 / dominant_frequency
print(f"Dominant frequency {dominant_frequency}")

if __name__ == "__main__":
    # Plot the original data and the harmonic fit
    plt.figure(figsize=(10, 6))
    plt.plot(time, signal, 'o', label='Signal Data', markersize=4)
    plt.plot(time, fit_signal_harmonic, 'o', label='Harmonic Fit', linewidth=1)
    plt.xlabel('Time(s)')
    plt.ylabel('Signal')
    plt.title('Harmonic Fit')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the magnitude of the FFT values
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies_positive, np.abs(fft_values_positive))
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Magnitude')
    plt.title('Fourier Spectrum of the Signal')
    plt.grid(True)
    plt.show()

    





