import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return np.sin(x)

a, b = 0, np.pi

N = 100000
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(y_rand)

quad_result, _ = quad(f, a, b)

print(f"Monte Carlo estimate: {monte_carlo_result}")
print(f"quad result: {quad_result}")
print(f"Absolute error: {abs(monte_carlo_result - quad_result)}")

x = np.linspace(a, b, 100)
plt.plot(x, f(x), label='f(x) = sin(x)')
plt.title('Function and Monte Carlo Integration')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()