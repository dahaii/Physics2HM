import numpy as np
import matplotlib.pyplot as plt

# Create a 10x10 matrix for potential values
matrix = np.zeros((10, 10))

# Constants
k = 8.99e9  # Coulomb's constant in N m^2/C^2
q = 5e-9    # Charge in C

# Calculate potential for each cell
for i in range(10):
    for j in range(10):
        r = np.sqrt(i**2 + j**2) * 0.1  # Distance in meters
        if r != 0:
            matrix[i, j] = k * q / r
        else:
            matrix[i, j] = np.inf  # Assign infinite potential at the location of the charge

# Plotting the electric potential distribution
plt.imshow(matrix, cmap='viridis', origin='lower', extent=[0, 1, 0, 1])
plt.colorbar(label='Electric Potential (V)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Electric Potential Distribution')

# Adding equipotential lines
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
X, Y = np.meshgrid(x, y)
plt.contour(X, Y, matrix, colors='white', levels=np.linspace(0, np.max(matrix[matrix != np.inf]), 10))

plt.show()

# Plot electric potential vs. X
x_values = np.arange(0, 1, 0.1)
v_values = matrix[:, 0]  # Potential values for j=0

plt.plot(x_values, v_values)
plt.xlabel('X')
plt.ylabel('Electric Potential (V)')
plt.title('Electric Potential vs. X')
plt.grid()
plt.show()

# Plot electric potential vs. diagonal distance
r_values = np.sqrt(np.arange(0, 10)**2 + np.arange(0, 10)**2) * 0.1

plt.plot(r_values, np.diag(matrix))
plt.xlabel('Diagonal Distance (m)')
plt.ylabel('Electric Potential (V)')
plt.title('Electric Potential vs. Diagonal Distance')
plt.grid()
plt.show()
