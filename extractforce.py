a=[]
force_x=[]
force_y=[]
force_z=[]

x_avg = 0
y_avg = 0
z_avg = 0

skip_next = False
reads = False
i = 0

with open('OUTCAR', 'r') as file:
    for line in file:
        if skip_next:
            # Skip this line and reset the flag
            skip_next = False
            continue
        
        if line.startswith("POSITION"):
            # Set the flag to skip the next line
            skip_next = True
            reads = True
            continue
            
        if reads == True and i < 134:
            a=line.strip().split()
            print(a)
            force_x.append(a[-3])
            force_y.append(a[-2])
            force_z.append(a[-1])
            a.clear()
            i = i + 1

x_avg = sum(force_x) / len(force_x)
y_avg = sum(force_y) / len(force_y)
z_avg = sum(force_z) / len(force_z)

with open("../forces.txt", "a") as ffile:
    ffile.write(x_avg+" "+y_avg+" "+z_avg+"\n")
    