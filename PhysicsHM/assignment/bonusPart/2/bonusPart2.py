import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Time Interval
t = np.linspace(0, 10, 1000)  # 1000 points between 0 and 10 seconds

# Time-varying Magnetic Field (B = B0 * sin(omega * t))
B0 = 1.0  # Maximum Magnetic Field (Tesla)
omega = 2 * np.pi * 0.5  # Angular Frequency (rad/s)
B = B0 * np.sin(omega * t)

# Loop Area (A = pi * r^2)
r = 0.1  # Radius (meter)
A = np.pi * r**2  # Area (square meter)

# Magnetic Flux (Φ = B * A)
phi = B * A

# Induced EMF (ε = -dΦ/dt)
dt = t[1] - t[0]  # Time Step
emk = -np.gradient(phi, dt)  # Alternative: emk = -B0 * A * omega * np.cos(omega * t)

# Static Plot
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Magnetic Field (T)', color='tab:blue')
ax1.plot(t, B, label='Magnetic Field (B)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Induced EMF (V)', color='tab:red')
ax2.plot(t, emk, label='Induced EMF (ε)', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.title('Electromagnetic Induction')
plt.show()

# Animated Plot
fig, ax = plt.subplots(figsize=(10, 6))

def update(i):
    ax.clear()
    B = B0 * np.sin(omega * t[:i])  # Update B until current frame
    phi = B * A
    if i > 1:  # Calculate EMF only after the first frame
        emk = -np.gradient(phi, t[:i])
    else:
        emk = np.zeros_like(phi)  # No EMF for the first frame
    ax.plot(t[:i], B[:i], label='Magnetic Field (B)', color='tab:blue')
    ax.plot(t[:i], emk[:i], label='Induced EMF (ε)', color='tab:red')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Magnetic Field (T)', color='tab:blue')
    ax.tick_params(axis='y', labelcolor='tab:blue')
    ax.legend()
    plt.title('Electromagnetic Induction')
    plt.tight_layout()
    return ax

ani = animation.FuncAnimation(fig, update, frames=len(t), interval=20)
plt.show()