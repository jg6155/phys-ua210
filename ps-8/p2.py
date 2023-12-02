from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#constants for the lorenz equations
sigma = 10
r = 28
b = 8 / 3


def lorenz(t, state):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = r * x - y - x * z
    dzdt = x * y - b * z
    return [dxdt, dydt, dzdt]

initial_conditions = [0, 1, 0]
t_range = (0, 50)
t_values = np.linspace(t_range[0], t_range[1], 10000)


solution = solve_ivp(lorenz, t_range, initial_conditions, t_eval=t_values)

x, y, z = solution.y

plt.figure(figsize=(12, 6))
plt.plot(solution.t, y)
plt.title('Lorenz Equations: y versus Time')
plt.xlabel('Time')
plt.ylabel('y')
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(x, z)
plt.title('Strange Attractor (z vs x)')
plt.xlabel('x')
plt.ylabel('z')
plt.show()