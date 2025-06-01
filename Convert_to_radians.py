import numpy as np
import glob
import os

# This script converts latitude and longitude from degrees to radians
# for all combined velocity files named as combined_<year>.txt.
# It outputs new files named combined_<year>_radians.txt with the converted coordinates.

years = range(85, 64, -1)

for year in years:
    input_pattern = f'combined_{year}.txt'
    output_file = f'combined_{year}_radians.txt'
    files = glob.glob(input_pattern)

    if not files:
        print(f"No files found for pattern: {input_pattern}")
        continue

    data = np.loadtxt(files[0])
    latitudes = data[:, 0]
    longitudes = data[:, 1]
    velocidades1 = data[:, 2]
    velocidades2 = data[:, 3]

    # Convert to radians
    latitudes_radianes = (90 - latitudes) * (np.pi / 180)
    longitudes_radianes = (longitudes + 360) * (np.pi / 180)

    data_radianes = np.column_stack((latitudes_radianes, longitudes_radianes, velocidades1, velocidades2))
    np.savetxt(output_file, data_radianes, fmt='%.6f')

