import csv
from ase.io import read
from nequip.ase import NequIPCalculator
from matplotlib import pyplot as plt

# === USER INPUT ===
model_path = "./compiled_model.nequip.pt2"                # Path to your deployed NequIP model
structures_path = "./sample_structures_posttrain.extxyz"      # Path to your .extxyz test set
output_csv = "./energy_comparison.csv"    # Output CSV file

# === 1. Load model on GPU ===
calc = NequIPCalculator.from_compiled_model(compile_path=model_path, chemical_symbols=["Cs", "Pb", "I"], device="cuda")  # Default is GPU if available

# === 2. Load test structures ===
structures = read(structures_path, ":")  # ":" loads all frames

# === 3. Loop through structures and collect energies ===
results = []
for i, atoms in enumerate(structures):
    # DFT reference energy (must be stored in atoms.info["energy"])
    E_dft = atoms.get_potential_energy()

    # MLIP-predicted energy
    atoms.calc = calc
    E_mlip = atoms.get_potential_energy()

    results.append([i, E_dft, E_mlip])

# === 4. Save to CSV ===
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Structure_Index", "E_DFT_eV", "E_MLIP_eV"])
    writer.writerows(results)

print(f"Saved energy comparison for {len(results)} structures to {output_csv}")