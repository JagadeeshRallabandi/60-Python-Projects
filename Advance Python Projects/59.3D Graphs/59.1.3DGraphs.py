import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data for a three-dimensional line
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

# Creating a new figure
fig = plt.figure()

# Adding a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plotting the 3D line
ax.plot3D(x, y, z, 'grey')

# Data for three-dimensional scattered points
z_scatter = 15 * np.random.random(100)
x_scatter = np.sin(z_scatter) + 0.1 * np.random.randn(100)
y_scatter = np.cos(z_scatter) + 0.1 * np.random.randn(100)

# Plotting the 3D scattered points
ax.scatter3D(x_scatter, y_scatter, z_scatter, c=z_scatter, cmap='Greens')

# Showing the plot
plt.show()
