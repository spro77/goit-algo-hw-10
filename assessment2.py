import matplotlib.pyplot as plt
import numpy as np

# Define the function and integration limits
def f(x):
    return np.sin(x)

a = 0  # Lower limit
b = np.pi  # Upper limit

# Create a range of x values for plotting
x = np.linspace(-0.5, np.pi + 0.5, 400)
y = f(x)

# Create the plot
fig, ax = plt.subplots()

# Plot the function
ax.plot(x, y, 'r', linewidth=2)

# Fill the area under the curve between a and b
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Configure the plot
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Add integration limits and title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()