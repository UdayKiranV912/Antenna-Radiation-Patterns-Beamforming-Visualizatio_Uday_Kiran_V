import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 2 * np.pi, 360)
phi = np.linspace(0, np.pi, 180)
theta_grid, phi_grid = np.meshgrid(theta, phi)

r1 = np.abs(np.cos(phi_grid))
r2 = np.abs(np.sin(phi_grid) * np.cos(theta_grid))
r3 = np.abs(np.sin(2 * phi_grid) * np.sin(2 * theta_grid))

x1 = r1 * np.sin(phi_grid) * np.cos(theta_grid)
y1 = r1 * np.sin(phi_grid) * np.sin(theta_grid)
z1 = r1 * np.cos(phi_grid)

x2 = r2 * np.sin(phi_grid) * np.cos(theta_grid)
y2 = r2 * np.sin(phi_grid) * np.sin(theta_grid)
z2 = r2 * np.cos(phi_grid)

x3 = r3 * np.sin(phi_grid) * np.cos(theta_grid)
y3 = r3 * np.sin(phi_grid) * np.sin(theta_grid)
z3 = r3 * np.cos(phi_grid)

fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(x1, y1, z1, cmap='viridis', alpha=0.9)
ax1.set_title('Isotropic-like Pattern')
ax1.axis('off')

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(x2, y2, z2, cmap='plasma', alpha=0.9)
ax2.set_title('Directional Pattern')
ax2.axis('off')

ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(x3, y3, z3, cmap='inferno', alpha=0.9)
ax3.set_title('Beamformed Pattern')
ax3.axis('off')

plt.tight_layout()
plt.show()

fig2 = plt.figure()
ax4 = fig2.add_subplot(111, polar=True)
gain = 10 * np.log10(np.abs(np.cos(theta - np.pi / 4))**2 + 0.1)
ax4.plot(theta, gain)
ax4.set_title("Polar Radiation Pattern")

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 2 * np.pi, 360)
phi = np.linspace(0, np.pi, 180)
theta_grid, phi_grid = np.meshgrid(theta, phi)

r1 = np.abs(np.sin(phi_grid) * np.cos(theta_grid))
r2 = np.abs(np.sin(2 * phi_grid) * np.sin(2 * theta_grid))
r3 = np.abs(np.cos(phi_grid))

x1 = r1 * np.sin(phi_grid) * np.cos(theta_grid)
y1 = r1 * np.sin(phi_grid) * np.sin(theta_grid)
z1 = r1 * np.cos(phi_grid)

x2 = r2 * np.sin(phi_grid) * np.cos(theta_grid)
y2 = r2 * np.sin(phi_grid) * np.sin(theta_grid)
z2 = r2 * np.cos(phi_grid)

x3 = r3 * np.sin(phi_grid) * np.cos(theta_grid)
y3 = r3 * np.sin(phi_grid) * np.sin(theta_grid)
z3 = r3 * np.cos(phi_grid)

fig1 = plt.figure(figsize=(18, 6))
ax1 = fig1.add_subplot(131, projection='3d')
ax1.plot_surface(x1, y1, z1, cmap='coolwarm')
ax1.set_title('Directional Pattern')
ax1.axis('off')

ax2 = fig1.add_subplot(132, projection='3d')
ax2.plot_surface(x2, y2, z2, cmap='magma')
ax2.set_title('Complex Pattern')
ax2.axis('off')

ax3 = fig1.add_subplot(133, projection='3d')
ax3.plot_surface(x3, y3, z3, cmap='plasma')
ax3.set_title('Isotropic Pattern')
ax3.axis('off')

plt.suptitle("3D Antenna Radiation Patterns", fontsize=16)
plt.tight_layout()
plt.show()

N = 8
d = 0.5
steering_angle = np.pi / 6
theta = np.linspace(0, 2 * np.pi, 1000)
response = np.abs(np.sum([np.exp(1j * 2 * np.pi * d * n * np.cos(theta - steering_angle)) for n in range(N)], axis=0))
response /= np.max(response)

fig2 = plt.figure(figsize=(7, 7))
ax4 = fig2.add_subplot(111, polar=True)
ax4.plot(theta, 20 * np.log10(response), color='darkorange', linewidth=2)
ax4.fill(theta, 20 * np.log10(response), alpha=0.3, color='orange')
ax4.set_title('Beamforming Array Pattern (Steered)', fontsize=14)
ax4.set_rlim(-30, 0)
ax4.grid(True)

plt.show()