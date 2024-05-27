# We examine shooting movements.

import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(F, angle_degrees):
    # Constants
    g = 9.81  # Gravitational acceleration (m/s^2)
    dt = 0.01  # Time step (s)

    # Convert angle to radians
    angle_radians = np.radians(angle_degrees)

    # Initial conditions
    v0_x = F * np.cos(angle_radians)  # Initial horizontal velocity
    v0_y = F * np.sin(angle_radians)  # Initial vertical velocity
    x, y = 0, 0  # Initial position

    # Simulate the motion
    x_list, y_list = [x], [y]
    while y >= 0:
        v_x = v0_x
        v_y = v0_y - g * dt
        x += v_x * dt
        y += v_y * dt
        x_list.append(x)
        y_list.append(y)
        v0_y = v_y

    # Plot the trajectory
    plt.plot(x_list, y_list)
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.title("Projectile Motion")
    plt.grid(True)
    plt.show()

# Get user inputs
try:
    F = float(input("Enter the force at launch (Newtons): "))
    angle = float(input("Enter the launch angle (0 to 90 degrees): "))
    if 0 < angle < 90:
        # Run the program
        projectile_motion(F, angle)
    else:
        print("Invalid angle value. Please enter an angle between 0 and 90 degrees.")
except ValueError:
    print("Invalid input. Please enter numeric values for force and angle.")
