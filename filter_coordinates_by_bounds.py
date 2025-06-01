import numpy as np
import glob

# This script filters latitude and longitude (in radians) from input files
# using predefined bounds for a specific study region.
# It reads files named combined_<year>_radians.txt and outputs
# filtered_<year}_radians.txt for each year in the specified range.

years = range(85, 64, -1)

for year in years:
    input_file = f'combined_{year}_radians.txt'
    output_file = f'filtered_{year}_radians.txt'

    if not glob.glob(input_file):
        print(f"No files found for pattern: {input_file}")
        continue

    data = np.loadtxt(input_file)

    # Filter data within latitude and longitude bounds (in radians)
    filtered_data = data[
        (data[:, 0] >= 0.78) & (data[:, 0] <= 2.01) &
        (data[:, 1] >= 4.13) & (data[:, 1] <= 5.63)
    ]

    np.savetxt(output_file, filtered_data, fmt='%.6f')

