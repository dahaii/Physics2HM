import numpy as np
import matplotlib.pyplot as plt

# Create a 10x10 matrix
matrix = np.zeros((10, 10))

# Constants
k = 8.99e9  # Coulomb's constant in N m^2/C^2
q = 5e-9    # Charge in C

# Calculate potential for each cell
for i in range(10):
    for j in range(10):
        r = np.sqrt(i**2 + j**2) * 0.1  # Distance in meters
        matrix[i, j] = k * q / r

plt.imshow(matrix, cmap='viridis', origin='lower', extent=[0, 1, 0, 1])
plt.colorbar(label='Electric Potential (V)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Electric Potential Distribution')
plt.show()

x_values = np.arange(0, 1, 0.1)
v_values = matrix[:, 0]  # Potential values for j=0

plt.plot(x_values, v_values)
plt.xlabel('X')
plt.ylabel('Electric Potential (V)')
plt.title('Electric Potential vs. X')
plt.grid()
plt.show()

r_values = np.sqrt(np.arange(0, 10)**2 + np.arange(0, 10)**2) * 0.1

plt.plot(r_values, np.diag(matrix))
plt.xlabel('Diagonal Distance (m)')
plt.ylabel('Electric Potential (V)')
plt.title('Electric Potential vs. Diagonal Distance')
plt.grid()
plt.show()


# In this electric potential distribution, points that have the same electric potential value are those located on the same equipotential surface.
# An equipotential surface is a surface where the electric potential is constant.
# Electric Potential Distribution Plot:
# The first plot shows the electric potential distribution across the 10x10 matrix. Darker regions represent higher potential values.
# The potential decreases as you move away from the central charge (located at the origin).
# The circular contours indicate equipotential surfaces.


# The f part is here:
# By using a finer grid (100x100), the equipotential lines become smoother and more detailed, providing a clearer representation of the potential distribution.

# Create a 100x100 matrix for a finer grid
matrix_fine = np.zeros((100, 100))

# Calculate potential for each cell in the finer grid
for i in range(100):
    for j in range(100):
        r = np.sqrt(i**2 + j**2) * 0.01  # Adjusted distance for finer grid
        if r != 0:
            matrix_fine[i, j] = k * q / r
        else:
            matrix_fine[i, j] = np.inf

# Plotting with finer grid
plt.imshow(matrix_fine, cmap='viridis', origin='lower', extent=[0, 1, 0, 1])
plt.colorbar(label='Electric Potential (V)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Electric Potential Distribution with Finer Grid')
plt.contour(np.linspace(0, 1, 100), np.linspace(0, 1, 100), matrix_fine, colors='white', levels=np.linspace(0, np.max(matrix_fine[matrix_fine != np.inf]), 20))
plt.show()


# Below is the code that has been modified and edited so that we can draw equipotential lines:
# aPartF.py
with open('aPartF.py') as file:
    exec(file.read())
