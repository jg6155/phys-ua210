from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import svd
import time

# Load the data
hdu_list = fits.open('ps-6/specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
wavelength = 10**logwave

# Plot a handful of galaxies
num_galaxies_to_plot = 5
plt.figure(figsize=(10, 6))
for i in range(num_galaxies_to_plot):
    plt.plot(wavelength, flux[i], label=f'Galaxy {i+1}')
plt.xlabel('Wavelength (Angstrom)')
plt.ylabel('Flux ($10^{-17}$ erg s$^{-1}$ cm$^{-2}$ Å$^{-1}$)')
plt.title('Spectra of a Handful of Galaxies')
plt.legend()
plt.show()

# Normalize the spectra
flux_sums = flux.sum(axis=1)
normalized_flux = flux / flux_sums[:, np.newaxis]

# Subtract the mean flux
mean_flux = np.mean(normalized_flux, axis=0)
residuals = normalized_flux - mean_flux
start_cov = time.time()
# Calculate the covariance matrix as R * R.T (assuming R is already mean-subtracted)
cov_matrix = np.dot(residuals.T, residuals) / (residuals.shape[0] - 1)
cov_time = time.time()-start_cov

# Calculate the eigenvectors and eigenvalues of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

# Sort the eigenvectors by decreasing eigenvalues
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvectors = eigenvectors[:, sorted_indices]
sorted_eigenvalues = eigenvalues[sorted_indices]


# Plot the first five eigenvectors
plt.figure(figsize=(15, 10))
for i in range(5):
    plt.plot(wavelength, sorted_eigenvectors[:, i], label=f'Eigenvector {i+1}')

plt.xlabel('Wavelength (Angstrom)')
plt.ylabel('Eigenvector Amplitude')
plt.title('First Five Eigenvectors from PCA of Galaxy Spectra')
plt.legend()
plt.show()

# Perform SVD on the residuals 
start_svd = time.time()
U, S, Vt = svd(residuals, full_matrices=False)
end_svd = time.time()
svd_time = end_svd - start_svd

# Print computational times
print(f"Time for eigendecomposition using covariance matrix: {cov_time} seconds")
print(f"Time for SVD: {svd_time} seconds")

# Plot the difference between the eigenvectors from the covariance matrix and SVD
plt.figure(figsize=(15, 10))
for i in range(5):
    # Adjusting signs if necessary for comparison
    sign_adjust = 1 if np.dot(sorted_eigenvectors[:, i], Vt[i, :]) > 0 else -1
    diff = sorted_eigenvectors[:, i] - sign_adjust * Vt[i, :]
    plt.plot(wavelength, diff, label=f'Difference in Eigenvector {i+1}')

plt.xlabel('Wavelength (Angstrom)')
plt.ylabel('Difference in Amplitude')
plt.title('Difference between Eigenvectors from Covariance Matrix and SVD')
plt.legend()
plt.show()
# Calculate and compare condition numbers
condition_number_cov = np.max(eigenvalues) / np.min(eigenvalues[eigenvalues > 0])
condition_number_svd = np.max(S) / np.min(S[S > 0])
print(f"Condition number of covariance matrix: {condition_number_cov}")
print(f"Condition number of SVD: {condition_number_svd}")

# Reconstruct the approximate spectra using the first five PCs
coefficients = np.dot(residuals, Vt[:5, :].T)
approx_spectra = np.dot(coefficients, Vt[:5, :])
approx_spectra += mean_flux
approx_spectra *= flux_sums[:, np.newaxis]

# Create scatter plots of the first three coefficients
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.scatter(coefficients[:, 0], coefficients[:, 1], alpha=0.7)
plt.xlabel('$c_0$')
plt.ylabel('$c_1$')
plt.title('$c_0$ vs $c_1$ for all galaxies')
plt.subplot(1, 2, 2)
plt.scatter(coefficients[:, 0], coefficients[:, 2], alpha=0.7)
plt.xlabel('$c_0$')
plt.ylabel('$c_2$')
plt.title('$c_0$ vs $c_2$ for all galaxies')
plt.tight_layout()
plt.show()
