import numpy as np
from shapely.geometry import Point, Polygon

# Define the polygon(s) where tracers will be placed (e.g., oceanic plates)
oceanic_plate = Polygon([
    # (y1, x1),
    # (y2, x2),
    # ...
])

# Define the spatial domain (in degrees) and grid resolution
y_min, y_max = 0.78, 2.01
x_min, x_max = 4.13, 5.63
step = 0.005  # grid step in degrees

# Generate a regular grid of points over the domain
ys = np.arange(y_min, y_max + step, step)
xs = np.arange(x_min, x_max + step, step)

points = []

# Check if each grid point falls within the defined polygon and assign tracer properties
for y in ys:
    for x in xs:
        p = Point(y, x)
        if oceanic_plate.contains(p):
            # Format: y, x, initial_temperature, initial_composition (or other scalar values)
            points.append((round(y, 4), round(x, 4), 0.9980, 0.0000))

# Write the tracer information to file
with open("tracers_ini.dat", "w") as f:
    for row in points:
        f.write("{:.4f} {:.4f} {:.4f} {:.4f}\n".format(*row))

