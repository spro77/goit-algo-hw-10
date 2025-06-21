import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def f(x):
    return np.sin(x)

a = 0
b = np.pi

N = 100000
x_rand = np.random.uniform(a, b, N)
mc_integral = (b - a) * np.mean(f(x_rand))

# Analytical integration using quad
quad_integral, _ = quad(f, a, b)

# Print results
print(f"Monte Carlo estimate: {mc_integral}")
print(f"quad result: {quad_integral}")
print(f"Absolute error: {abs(mc_integral - quad_integral)}")

x = np.linspace(-0.5, np.pi + 0.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()