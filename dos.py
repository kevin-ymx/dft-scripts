import numpy as np
from py4vasp import Calculation

calc=Calculation.from_path("./")

dos=calc.dos.read(selection="p(Ba)")
E=dos['energies']
totalu=dos['up']
totald=dos['down']
total=totalu+totald
Ba_p_u=dos['Ba_p_up']
Ba_p_d=dos['Ba_p_down']
Ba_p=Ba_p_u+Ba_p_d
dos.clear()

dos=calc.dos.read(selection="d(Ba)")
Ba_d_u=dos['Ba_d_up']
Ba_d_d=dos['Ba_d_down']
Ba_d=Ba_d_u+Ba_d_d
dos.clear()

dos=calc.dos.read(selection="s(Sn)")
Sn_s_u=dos['Sn_s_up']
Sn_s_d=dos['Sn_s_down']
Sn_s=Sn_s_u+Sn_s_d
dos.clear()

dos=calc.dos.read(selection="p(Sn)")
Sn_p_u=dos['Sn_p_up']
Sn_p_d=dos['Sn_p_down']
Sn_p=Sn_p_u+Sn_p_d
dos.clear()

dos=calc.dos.read(selection="d(Sn)")
Sn_d_u=dos['Sn_d_up']
Sn_d_d=dos['Sn_d_down']
Sn_d=Sn_d_u+Sn_d_d
dos.clear()

dos=calc.dos.read(selection="s(Nb)")
Nb_s_u=dos['Nb_s_up']
Nb_s_d=dos['Nb_s_down']
Nb_s=Nb_s_u+Nb_s_d
dos.clear()

dos=calc.dos.read(selection="p(Nb)")
Nb_p_u=dos['Nb_p_up']
Nb_p_d=dos['Nb_p_down']
Nb_p=Nb_p_u+Nb_p_d
dos.clear()

dos=calc.dos.read(selection="d(Nb)")
Nb_d_u=dos['Nb_d_up']
Nb_d_d=dos['Nb_d_down']
Nb_d=Nb_d_u+Nb_d_d
dos.clear()

dos=calc.dos.read(selection="s(O)")
O_s_u=dos['O_s_up']
O_s_d=dos['O_s_down']
O_s=O_s_u+O_s_d
dos.clear()

dos=calc.dos.read(selection="p(O)")
O_p_u=dos['O_p_up']
O_p_d=dos['O_p_down']
O_p=O_p_u+O_p_d
dos.clear()

dos_raw=np.array([E,total,Ba_p,Ba_d,Sn_s,Sn_p,Sn_d,Nb_s,Nb_p,Nb_d,O_s,O_p])
dos=np.transpose(dos_raw)
np.savetxt('pdos.txt', dos, delimiter =' ')
