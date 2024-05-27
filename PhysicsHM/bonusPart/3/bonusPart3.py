import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Time and Space Intervals
x = np.linspace(0, 4 * np.pi, 1000)  # 1000 points between 0 and 4π
t = np.linspace(0, 2 * np.pi, 200)   # 200 time steps between 0 and 2π

# Wave Parameters
A = 1.0  # Amplitude
k = 1.0  # Wavenumber
omega = 1.0  # Angular frequency

def wave1(x, t):
    return A * np.sin(k * x - omega * t)

def wave2(x, t):
    return A * np.sin(k * x + omega * t)

def superposition(x, t):
    return wave1(x, t) + wave2(x, t)

fig, ax = plt.subplots(figsize=(10, 6))

def update(frame):
    ax.clear()
    y1 = wave1(x, t[frame])
    y2 = wave2(x, t[frame])
    y_super = superposition(x, t[frame])
    ax.plot(x, y1, label='Wave 1')
    ax.plot(x, y2, label='Wave 2')
    ax.plot(x, y_super, label='Superposition')
    ax.set_xlabel('Space (x)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Wave Motion and Superposition')
    ax.legend()
    ax.set_ylim(-2 * A, 2 * A)
    return ax

ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50)
plt.show()