import pandas as pd
from shapely.geometry import Point, Polygon

df = pd.read_csv("velocidades.dat", header=None)

# Polygons for each oceanic region where preexisting slabs will be generated.
# Coordinates must be placed inside the brackets ([...]) of each polygon.
farallon_polygon = Polygon([...])     # Trench along the Pacific
atlantica1_polygon = Polygon([...])   # Caribbean Great Arc (GAC)
atlantica2_polygon = Polygon([...])   # Aves Trench (TA)

vx_list = []
vy_list = []

for _, row in df.iterrows():
    point = Point(row['x'], row['y'])

    # Synthetic velocities
    if farallon_polygon.contains(point):
        vx_list.append(2.62)
        vy_list.append(-4.25)
    elif atlantica1_polygon.contains(point):
        vx_list.append(-2.62)
        vy_list.append(4.25)
    elif atlantica2_polygon.contains(point):
        vx_list.append(-1.67)
        vy_list.append(1.086)
    else:
        vx_list.append(0)
        vy_list.append(0)

vel_df = pd.DataFrame({
    "vx": vx_list,
    "vy": vy_list
})
vel_df.to_csv("synthetic_velocities.csv", index=False, header=False)

