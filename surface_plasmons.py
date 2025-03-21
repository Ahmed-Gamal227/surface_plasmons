import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
radius = 1.0  # Radius of the nanoparticle (arbitrary units)
n_points = 100  # Number of points around the circle
frequency = 2.0  # Oscillation frequency
frames = 100  # Number of animation frames

# Create a circle representing the nanoparticle
theta = np.linspace(0, 2 * np.pi, n_points)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)

# Electric field parameters (external light wave)
field_amplitude = 0.5
field_x = np.linspace(-2 * radius, 2 * radius, 500)

# Initialize figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_title("Surface Plasmon Oscillation")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Plot the nanoparticle and field
particle, = ax.plot(x_circle, y_circle, 'k', linewidth=2, label="Nanoparticle")
electrons, = ax.plot([], [], 'bo', label="Electron Oscillations")
field_line, = ax.plot([], [], 'r--', label="Electric Field")

# Initialize empty electron positions
electron_positions_x = []
electron_positions_y = []

# Animation update function
def update(frame):
    global electron_positions_x, electron_positions_y
    # Update electron positions (oscillation)
    displacement = field_amplitude * np.sin(2 * np.pi * frequency * frame / frames)
    electron_positions_x = (radius + displacement) * np.cos(theta)
    electron_positions_y = (radius + displacement) * np.sin(theta)
    
    # Update electric field
    field_y = field_amplitude * np.sin(2 * np.pi * frequency * field_x + frame / frames * 2 * np.pi)
    
    # Update plots
    electrons.set_data(electron_positions_x, electron_positions_y)
    field_line.set_data(field_x, field_y)
    return particle, electrons, field_line

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Display animation
plt.legend()
plt.show()
