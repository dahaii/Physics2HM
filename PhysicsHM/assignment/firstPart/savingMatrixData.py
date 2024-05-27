import numpy as np

# Constants
k = 8.9875e9  # Coulomb's constant in Nm^2/C^2
q = 5e-9      # Charge in Coulombs

# Create a 10x10 matrix
matrix_size = 10
matrix = np.zeros((matrix_size, matrix_size))

# Define function to calculate electric potential at a point
def electric_potential(x, y):
    distance = np.sqrt(x**2 + y**2) * 0.1  # distance from charge in meters
    potential = k * q / distance
    return potential

# Calculate electric potential at each point in the matrix
for i in range(matrix_size):
    for j in range(matrix_size):
        if i == 0 and j == 0:  # Skip the point charge itself
            continue
        matrix[i][j] = electric_potential(i, j)

# Save the calculated potentials
np.savetxt("electricPotentials.csv", matrix, delimiter=",")

# Print the matrix
print(matrix)
