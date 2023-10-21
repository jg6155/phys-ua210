import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('../signal.dat', delimiter='|', skiprows=1, usecols=(1, 2))
time, signal = data[:, 0], data[:, 1]
# Plot the data
if __name__ == "__main__":
    plt.figure(figsize=(10, 6))
    plt.plot(time, signal, 'o', label='Signal Data', markersize=4)
    plt.xlabel('Time(s)')
    plt.ylabel('Signal')
    plt.title('Signal vs. Time')
    plt.legend()
    plt.grid(True)
    plt.show()

