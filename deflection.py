from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np


# Everything uses SI base units (kg, m, N, etc)

carriage_mass = 1.0
F = carriage_mass * 9.81

X_len = 0.26
Y_len = 0.3

num_x_rods = 2
num_y_rods = 2

# Young's modulus of aluminum
E = 69e9

rod_diam = 0.008

# Area moment of inertia
I = np.pi * (rod_diam ** 4) / 64

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

X = np.linspace(0, 0.26, 100)
Y = np.linspace(0, 0.3, 100)
X, Y = np.meshgrid(X, Y)

deflect_x = ((F / num_x_rods) * X**3 * (X_len - X) ** 3) / (3 * X_len ** 3 * E * I)
deflect_y = ((F / num_y_rods) * Y**3 * (Y_len - Y) ** 3) / (3 * Y_len ** 3 * E * I)

Z = np.sqrt(deflect_x + deflect_y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_xlabel("X")
ax.set_ylabel("Y")

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
