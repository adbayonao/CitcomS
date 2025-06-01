import pandas as pd
import numpy as np
from shapely.geometry import Point, Polygon

df = pd.read_csv("velocidades.csv", header=None)
ages = []

# Coordinates of tectonic plates taken from GPlates,
# which should be placed inside the brackets ([...]) of each polygon.
farallon_polygon = Polygon([...])        # Farallon, 40 Ma
atlantico_polygon = Polygon([...])       # Atlantic, 40 Ma
norteamericana_polygon = Polygon([...])  # North America continental, 100 Ma
suramericana_polygon = Polygon([...])    # South America continental, 100 Ma
caribe_polygon = Polygon([...])          # Caribbean, 70 Ma
buffer_polygon = Polygon([...])          # Buffer zone, 5 Ma
debilidad_polygon = Polygon([...])       # Weakness zone, 5 Ma

for _, row in df.iterrows():
    point = Point(row['x'], row['y'])

    if buffer_polygon.contains(point):
        ages.append(5)
    elif debilidad_polygon.contains(point):
        ages.append(5)
    elif farallon_polygon.contains(point):
        ages.append(40)
    elif atlantico_polygon.contains(point):
        ages.append(40)
    elif caribe_polygon.contains(point):
        ages.append(70)
    elif norteamericana_polygon.contains(point):
        ages.append(100)
    elif suramericana_polygon.contains(point):
        ages.append(100)
    else:
        ages.append(np.nan)

ages_df = pd.DataFrame(ages)
ages_df.to_csv("edades_placas_tectónicas.dat", index=False, header=False)

