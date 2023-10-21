import numpy as np
import matplotlib.pyplot as plt

# Define the function for the integrand
def integrand(x, n):
    return x**(n-1) * np.exp(-x)

# Generate x values
x_values = np.linspace(0, 5, 500)

# Calculate y values for different n
y_values_n2 = integrand(x_values, 2)
y_values_n3 = integrand(x_values, 3)
y_values_n4 = integrand(x_values, 4)

# Plot
plt.figure(figsize=(10,6))
plt.plot(x_values, y_values_n2, label='n=2')
plt.plot(x_values, y_values_n3, label='n=3')
plt.plot(x_values, y_values_n4, label='n=4')
plt.title('Integrand $x^{n-1} e^{-x}$ for different n')
plt.xlabel('x')
plt.ylabel('Integrand value')
plt.legend()
plt.grid(True)
plt.show()
