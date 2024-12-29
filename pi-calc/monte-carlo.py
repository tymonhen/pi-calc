import numpy as np
import matplotlib.pyplot as plt

num_p = 100000

x = np.random.uniform(0, 1, num_p)
y = np.random.uniform(0, 1, num_p)

dist = x**2 + y**2

in_circ = dist <= 1

pi_estimate = 4 * np.sum(in_circ) / num_p

plt.figure(figsize=(6, 6))
plt.scatter(x[in_circ], y[in_circ], color='red', s=1, label="Inside Circle")
plt.scatter(x[~in_circ], y[~in_circ], color='blue', s=1, label="Outside Circle")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')

circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
plt.gca().add_artist(circle)

plt.title(f"Monte Carlo Approximation of Pi\n: {pi_estimate:.10f}")
plt.legend()
plt.show()
