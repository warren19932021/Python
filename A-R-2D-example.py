import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import the 3D plotting toolkit
from matplotlib.colors import Normalize
from scipy.optimize import minimize

# Define your function MyFunction in Python
def MyFunction(params):
    Va, Vb = params
    lamda1 = 0.0000123
    lamda2 = 0.5
    lamda3 = 0.35

    f = 1e7 * lamda1 * np.cos(Vb) * \
        np.power(1.0 - 0.075 * (lamda1 * (1000.0 * (1.0 / np.cos(Vb)) - 100) / (lamda2 * (Va + lamda1 * 1000.0 * (1.0 / np.cos(Vb) - 0.1)) * (1.0 / lamda2))), lamda3 / ((lamda2 * (Va + lamda1 * 1000.0 * (1.0 / np.cos(Vb) - 0.1)) * (1.0 / lamda2) + 0.25) * np.cos(Vb))) / ((Va + lamda1 * 1000.0 * (1.0 / np.cos(Vb) - 0.1)) * (1.0 / lamda2) * np.cos(Vb) + 15)

    return f

# Set bounds for Va and Vb
bounds = [(0, 10), (0, np.pi / 2)]

# Optimize to find the maximum value
def NegativeFunction(params):
    return -MyFunction(params)

result = minimize(NegativeFunction, x0=(5, np.pi / 4), bounds=bounds, method='L-BFGS-B')
max_N = -result.fun  # Maximum value of f
optimal_params = result.x

# Increase the number of samples
num_samples = 500000

# Generate samples using acceptance-rejection sampling with adaptive sampling strategy
samples = []

while len(samples) < num_samples:
    Va = np.random.uniform(bounds[0][0], bounds[0][1])
    Vb = np.random.uniform(bounds[1][0], bounds[1][1])
    u = np.random.uniform(0, 1)

    # Adjust the threshold based on local maximum
    local_max = MyFunction([Va, Vb])
    threshold = max_N * local_max / max_N

    if u * threshold <= MyFunction([Va, Vb]):
        samples.append([Va, Vb])

# Convert samples to numpy array for easier manipulation
samples = np.array(samples)

# Create a figure to compare the target distribution and generated samples
fig = plt.figure(figsize=(12, 6))

# Plot the target distribution (MyFunction) in 3D style
ax1 = fig.add_subplot(121, projection='3d')
Va_grid, Vb_grid = np.meshgrid(np.linspace(bounds[0][0], bounds[0][1], 200), np.linspace(bounds[1][0], bounds[1][1], 200))
N_grid = MyFunction([Va_grid, Vb_grid])

# Adjust the Z-axis range
ax1.set_zlim(0, max_N)

# Use a different colormap for better contrast
norm = Normalize(vmin=0, vmax=max_N)
ax1.plot_surface(Va_grid, Vb_grid, N_grid, cmap='coolwarm', norm=norm)
ax1.set_title('Target Distribution (MyFunction)')

# Plot the generated samples in 3D
ax2 = fig.add_subplot(122, projection='3d')  # Create a 3D subplot
ax2.scatter(samples[:, 0], samples[:, 1], MyFunction(samples.T), c=samples[:, 1], cmap='Blues')
ax2.set_xlabel('Va')
ax2.set_ylabel('Vb')
ax2.set_zlabel('Function Value')
ax2.set_title('Generated Samples')

plt.tight_layout()
plt.show()

