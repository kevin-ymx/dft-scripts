#!/bin/bash

# List of directories (absolute or relative paths)
dirs=(
    "0.0"
    "10.0"
    "-10.0"
    "20.0"
    "-20.0"
    "40.0"
    "-40.0"
)

# Loop through each directory
for d in "${dirs[@]}"; do
    echo "=== Entering directory: /pscratch/sd/y/yeming/MLMD/AIMD_CsPbI3/v_I_D4h_Pb3.20_0/Bond_Distortion_$d% ==="
    cd "/pscratch/sd/y/yeming/MLMD/AIMD_CsPbI3/v_I_D4h_Pb3.20_0/Bond_Distortion_$d%" || { echo "Failed to enter /pscratch/sd/y/yeming/MLMD/AIMD_CsPbI3/v_I_D4h_Pb3.20_0/Bond_Distortion_$d%"; exit 1; }

    # === First modification ===
    echo "Applying first modification to sample_struc.py..."
    # Example: replace 'param = 1' with 'param = 2'
    sed -i 's/sample_struc_posttrain.xyz/train.xyz/' sample_struc.py
    sed -i 's/size = 5/size = 24/' sample_struc.py

    # Run the script
    echo "Running script (first run)..."
    python sample_struc.py

    # === Second modification ===
    echo "Applying second modification to sample_struc.py..."
    # Example: replace 'param = 2' with 'param = 3'
    sed -i 's/train.xyz/val.xyz/' sample_struc.py
    sed -i 's/size = 24/size = 3/' sample_struc.py

    # Run the script again
    echo "Running script (second run)..."
    python sample_struc.py

    echo "=== Finished directory: /pscratch/sd/y/yeming/MLMD/AIMD_CsPbI3/v_I_D4h_Pb3.20_0/Bond_Distortion_$d% ==="
    echo
done
