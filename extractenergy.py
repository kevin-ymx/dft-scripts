a=[]
energy=[]
with open('OUTCAR', 'r') as file:
    for line in file:
        if line.startswith("  energy  without entropy="):
            a=line.strip().split()
            energy.append(a[-1])
            a.clear()
        else:
            continue
            
with open("../energies.txt", "a") as efile:
    efile.write(energy[-1]+"\n")
    