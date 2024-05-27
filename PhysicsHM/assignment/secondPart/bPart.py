import numpy as np
import matplotlib.pyplot as plt

# Space and Time Definitions
x = np.linspace(0, 4 * np.pi, 1000)  # 1000 points between 0 and 4π
t = 0  # Initial time

# Wave Parameters
A1, A2 = 1, 1  # Amplitudes
k1, k2 = 1, 1  # Wavenumbers
omega1, omega2 = 1, 1  # Angular Frequencies
phi1, phi2 = 0, np.pi / 2  # Phases

# Wave Functions
y1 = A1 * np.sin(k1 * x - omega1 * t + phi1)
y2 = A2 * np.sin(k2 * x - omega2 * t + phi2)

y_total = y1 + y2

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Wave 1')
plt.plot(x, y2, label='Wave 2')
plt.plot(x, y_total, label='Total Interference')
plt.title('Wave Motion and Interference')
plt.xlabel('Space (x)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Animated Plot
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(10, 6))

def update(t):
    ax.clear()
    y1 = A1 * np.sin(k1 * x - omega1 * t + phi1)
    y2 = A2 * np.sin(k2 * x - omega2 * t + phi2)
    y_total = y1 + y2
    ax.plot(x, y1, label='Wave 1')
    ax.plot(x, y2, label='Wave 2')
    ax.plot(x, y_total, label='Total Interference')
    ax.set_title('Wave Motion and Interference')
    ax.set_xlabel('Space (x)')
    ax.set_ylabel('Amplitude')
    ax.legend()
    ax.grid(True)
    return ax

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 200), interval=50)
plt.show()