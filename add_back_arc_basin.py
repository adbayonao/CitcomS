import pandas as pd
from shapely.geometry import Point, Polygon

# Load velocity and coordinate data
vel_df = pd.read_csv("velocidades.dat", header=None)
coord_df = pd.read_csv("coordenadas.dat", header=None)

# Check that both files have the same number of rows
assert len(vel_df) == len(coord_df), "The number of rows in the velocity and coordinate files do not match."

# Define the polygon for the Granada Back-Arc Basin region
backarc_polygon = Polygon([
    # Add coordinates here, e.g., (lon1, lat1), (lon2, lat2), ...
])

new_vx = []
new_vy = []

# Assign synthetic velocities within the back-arc polygon
for i in range(len(coord_df)):
    point = Point(coord_df.iloc[i][0], coord_df.iloc[i][1])  # Assuming columns are [x, y]
    
    if backarc_polygon.contains(point):
        new_vx.append(5.0)   # Synthetic velocity in x
        new_vy.append(0.0)   # Synthetic velocity in y
    else:
        new_vx.append(vel_df.iloc[i][0])  # Original velocity x
        new_vy.append(vel_df.iloc[i][1])  # Original velocity y

# Save updated velocities to a new file
output_df = pd.DataFrame({
    "vx": new_vx,
    "vy": new_vy
})
output_df.to_csv("velocidades_Cuenca_de_Granada.dat", index=False, header=False)

