import numpy as np

# This script combines multiple coordinate files (from GPlates polygons)
# with their corresponding velocity files into single output files.
# It is useful when the study area is large and spans several GPlates polygons.

coordenadas_files = [f'coordenadas_{i}.txt' for i in range(6, 11)]

for velocidad_group in range(85, 64, -1):
    for i in range(6, 11):
        coords = np.loadtxt(f'coordenadas_{i}.txt')
        velocidad = np.loadtxt(f'bvel{velocidad_group}.{i}')
        
        if coords.shape[0] != velocidad.shape[0]:
            print(f"Error: Files coordenadas_{i}.txt and bvel{velocidad_group}.{i} do not have the same number of lines.")
            continue
        
        combined_data = np.hstack((coords, velocidad))
        output_filename = f'combined_{velocidad_group}_{i}.txt'
        np.savetxt(output_filename, combined_data, fmt='%.6f')

