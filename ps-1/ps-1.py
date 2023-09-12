import numpy as np
import matplotlib.pyplot as plt

mu = 0
sigma = 3

x = np.linspace(-10,10,1000)

y = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(- (x - mu)**2 / (2 * sigma**2))

plt.plot(x,y)
plt.title("Gaussian Distribution")
plt.xlabel("x")
plt.ylabel("Probabilitiy Density")
plt.grid(True)
plt.tight_layout()
plt.savefig("gaussian.png")