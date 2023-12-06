import numpy as np
import matplotlib.pyplot as plt

M = 412800
g = 9.8
ro = 1.225
S = 541
b = 64

Cd0 = 0.02
e = 0.8

A = b*b/S
Vloss = 78.13
Vcrui = 259.17
Cl = 0
Cd = 0
Tr = 0
P = 0

n = (Vcrui - Vloss) / 9

def calculate(i):
    global Vvari
    if(i == 0):
        Vvari = round(Vloss, 6)
    else:
        Vvari = round((Vvari + n), 6)
    Cl = round((2 * (M * g) / (ro * Vvari*Vvari * S)), 6)
    Cd = round((Cd0 + ((Cl*Cl) / (np.pi * A * e))), 6)
    Tr = round(((M * g) / (Cl / Cd)),6)
    P = round(Tr * Vvari,6)
    return Vvari, Cl, Cd, Tr, P


Cd_values = []
Cl_values = []
Vvari_values = []
Tr_values = []
P_values = []

for i in range(10):
    Vvari, Cl, Cd, Tr, P = calculate(i)
    Cd_values.append(Cd)
    Cl_values.append(Cl)
    Vvari_values.append(Vvari)
    Tr_values.append(Tr)
    P_values.append(P)

print("{:<10}\t{:<10}\t{:<10}\t".format("V (m/s)", "Cl", "Cd"))
for i in range(10):
    Vvari, Cl, Cd, _, _ = calculate(i)
    print("{:<10}\t{:<10}\t{:<10}\t".format(Vvari, Cl, Cd))
    
plt.figure(figsize=(8, 6))
plt.plot(Cd_values, Cl_values, marker='o', linestyle='-', color='b')
plt.xlabel('Cd')
plt.ylabel('Cl')
plt.title('Cd & Cl')
plt.grid(True)
plt.show()    

print("{:<10}\t{:<10}\t".format("V (m/s)", "T (N)"))
for i in range(10):
    Vvari, _, _, Tr, _ = calculate(i)
    print("{:<10}\t{:<10}\t".format(Vvari, Tr))
    
plt.figure(figsize=(8, 6))
plt.plot(Vvari_values, Tr_values, marker='o', linestyle='-', color='g')
plt.xlabel('V (m/s)')
plt.ylabel('T (N)')
plt.title('V & T')
plt.grid(True)
plt.show()
    
print("{:<10}\t{:<10}\t".format("V (m/s)", "P (W)"))
for i in range(10):
    Vvari, _, _, _, P = calculate(i)
    print("{:<10}\t{:<10}\t".format(Vvari, P))
    
plt.figure(figsize=(8, 6))
plt.plot(Vvari_values, P_values, marker='o', linestyle='-', color='r')
plt.xlabel('V (m/s)')
plt.ylabel('P (W)')
plt.title('V & P')
plt.grid(True)
plt.show()
