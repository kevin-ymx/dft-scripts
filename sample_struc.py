import numpy as np

input_file = "trajectory.xyz"
output_file = "sample_struc.xyz"

lines_per_struc = 137

with open(input_file, 'r') as file:
    lines = file.readlines()

with open(output_file, 'w') as file:
    for i in np.random.randint(1500, int(len(lines)/137), size = 30):
        line_start = i * lines_per_struc
        line_end = line_start + lines_per_struc
        file.writelines(lines[line_start:line_end])