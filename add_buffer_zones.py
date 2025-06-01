import numpy as np

def process_files(input_filename, output_filename):
    # Load input data
    data = np.loadtxt(input_filename)

    x_coords = data[:, 0]
    y_coords = data[:, 1]
    vel = data[:, 2]

    new_vel_x = []
    new_vel_y = []

    # Initialize counters
    start_index = 0
    rows_to_copy = 183
    cycle_length = 257  # Not used in this version, but kept for reference

    # Add buffer zones (zero velocity) before and after each data block
    while start_index < len(vel):
        new_vel_x.extend([0] * 37)
        new_vel_y.extend([0] * 37)

        end_index = min(start_index + rows_to_copy, len(vel))
        new_vel_x.extend(vel[start_index:end_index])
        new_vel_y.extend(vel[start_index:end_index])

        start_index = end_index

        new_vel_x.extend([0] * 37)
        new_vel_y.extend([0] * 37)

    # Combine data and save to output file
    combined_data = np.column_stack((x_coords, y_coords, new_vel_x, new_vel_y))
    np.savetxt(output_filename, combined_data, fmt="%.6f", header="X Y Vel_X Vel_Y", comments='')

# Input and output filenames
input_file = "filtered_85_radians_coords_vel_x_sorted.dat"  # Repeat for each time step
output_file = "processed_velocities.dat"

# Run the function
process_files(input_file, output_file)

