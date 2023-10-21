import matplotlib.pyplot as plt
from part_b import time_scaled, signal
from part_d import fit_polynomial
# Explore different polynomial orders and their condition numbers
orders = list(range(1, 21))  # Exploring polynomials from 1st to 20th order
condition_numbers = []

for order in orders:
    _, cond_num, _ = fit_polynomial(time_scaled, signal, order)
    condition_numbers.append(cond_num)

# Plot condition numbers for different polynomial orders
if __name__ == "__main__":
    plt.figure(figsize=(10, 6))
    plt.plot(orders, condition_numbers, 'o-', markersize=4)
    plt.xlabel('Polynomial Order')
    plt.ylabel('Condition Number')
    plt.title('Condition Number vs. Polynomial Order')
    plt.grid(True)
    plt.show()
