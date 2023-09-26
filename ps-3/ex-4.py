import numpy as np
import matplotlib.pyplot as plt

T_half_life_Tl208 = 3.053
lambda_Tl208 = np.log(2) / T_half_life_Tl208

num_atoms = 1000
random_numbers = np.random.random(num_atoms)
decay_times = -np.log(1 - random_numbers) / lambda_Tl208

sorted_decay_times = np.sort(decay_times)

times = np.linspace(0, max(sorted_decay_times), 1000)
not_decayed = [np.sum(sorted_decay_times > t) for t in times]

plt.figure(figsize=(10, 6))
plt.plot(times, not_decayed, label='Number of Atoms Not Decayed', color='blue')
plt.xlabel('Time (minutes)')
plt.ylabel('Number of Atoms')
plt.title('Decay of $^{208}$Tl Atoms Over Time')
plt.legend()
plt.grid(True)
plt.show()