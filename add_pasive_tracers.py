import numpy as np
from shapely.geometry import Point, Polygon

# Coordinates defining the Gran Caribbean Arc region polygon (Y, X)
polygon_coords = [
    (1.271, 4.973),
    (1.007, 5.149),
    (1.132, 5.330),
    (1.362, 5.159),
    (1.271, 4.973)  # Close the polygon by repeating the first point
]

polygon = Polygon(polygon_coords)

# Create a buffer around the polygon for tolerance in point inclusion
tolerance = 0.0005
expanded_polygon = polygon.buffer(tolerance)

# Depth range and step for passive tracer placement
depth_min = 0.9800
depth_max = 0.9980
depth_step = 0.002

# Input and output tracer files
input_filename = "tracers_ini.dat"
output_filename = "tracers_modified.dat"

# Read existing tracers
with open(input_filename, "r") as file:
    lines = file.readlines()

all_lines = []  # Will contain original + added tracers
new_lines = []  # New passive tracers inside the polygon

filter_step = 3  # Keep one out of every 3 lines for efficiency

for i, line in enumerate(lines):
    # Filter lines to reduce number of points processed
    if i % filter_step != 0:
        continue
    
    columns = line.split()
    y = float(columns[1])
    x = float(columns[0])
    point = Point(x, y)
    
    all_lines.append(line)  # Keep original tracer
    
    # If point is inside the expanded polygon, add passive tracers at different depths
    if expanded_polygon.contains(point):
        for depth in np.arange(depth_max, depth_min - depth_step, -depth_step):
            new_line = f"{x:.4f} {y:.4f} {depth:.4f} 2.0000\n"
            new_lines.append(new_line)

# Append all new passive tracers to the output
all_lines.extend(new_lines)

# Write all tracers to the output file
with open(output_filename, "w") as file:
    file.writelines(all_lines)

