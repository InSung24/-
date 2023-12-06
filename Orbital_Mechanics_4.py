import numpy as np

n = 2 * np.pi / (720 * 60)
e = 0.75
a = 26610
h = n*a*a*np.sqrt(1-e*e)

def calculate(i):
    tc = i * 30 * 60
    t = i * 30
    
    ai = (63.4)*(np.pi/180)
    aomm = (45)*(np.pi/180)
    aomg = (270)*(np.pi/180)
    
    #E
    E = 2 * np.pi * i / 25
    while True:
        E_new = E - (E - e * np.sin(E) - n * tc) / (1 - e * np.cos(E))
        if np.abs(E_new - E) < 1e-10:
            E = E_new
            break
        E = E_new
    E_degree = round(np.degrees(E),1)
    
    #M
    M = E - e * np.sin(E)
    M_degree = round(np.degrees(M),1)
    
    #f
    f = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    
    #r
    r = a * (1 - e * np.cos(E))
    
    #v
    v = n * a * np.sqrt((1 + e * np.cos(E)) / (1 - e * np.cos(E)))
    
    #pi
    p = np.arctan(e * np.sin(E) / np.sqrt(1 - e **2))
    if i<13:
        p_degree = round((np.degrees(p) % 360),1)
    else:
        p_degree = round((np.degrees(p) % 360) - 360,1)
        
        
    drdt = (h*e*np.sin(f))/(a*(1-e*e))
    R11 = np.cos(aomm)*np.cos(aomg+f) - np.sin(aomm)*np.sin(aomg+f)*np.cos(ai)
    R21 = np.sin(aomm)*np.cos(aomg+f) + np.cos(aomm)*np.sin(aomg+f)*np.cos(ai)
    R31 = np.sin(aomg+f)*np.sin(ai)
    
    R12 = -np.cos(aomm)*np.sin(aomg+f) - np.sin(aomm)*np.cos(aomg+f)*np.cos(ai)
    R22 = -np.sin(aomm)*np.sin(aomg+f) + np.cos(aomm)*np.cos(aomg+f)*np.cos(ai)
    R32 = np.cos(aomg+f)*np.sin(ai)
    
    #r
    r_x = round(r*R11,0)
    r_y = round(r*R21,0)
    r_z = round(r*R31,0)
    
    #v
    v_x = round((drdt*R11) + ((h/r)*R12), 1) 
    v_y = round((drdt*R21) + ((h/r)*R22), 1)
    v_z = round((drdt*R31) + ((h/r)*R32), 1)

    return t, r_x, r_y, r_z, v_x, v_y, v_z

print("{:<12}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format("t-t0 (min)", "r_x (km)", "r_y (km)", 
                                                                      "r_z (km)", "v_x (km/s)", "v_y (km/s)", "v_z (km/s)"))
for i in range(0, 25):
    t, r_x, r_y, r_z, v_x, v_y, v_z = calculate(i)
    print("{:<12}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format(t, r_x, r_y, r_z, v_x, v_y, v_z))
