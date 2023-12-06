import numpy as np

n = 2 * np.pi / (720 * 60)
e = 0.75
a = 26610

def calculate(i):
    tc = i * 30 * 60
    t = i * 30
    
    E = 2 * np.pi * i / 25
    
    #E
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
    f_degree = round(np.degrees(f),1)
    
    #r
    r = a * (1 - e * np.cos(E))
    r_c = round(r,0)
    
    #v
    v = n * a * np.sqrt((1 + e * np.cos(E)) / (1 - e * np.cos(E)))
    v_c = round(v,2)
    
    #pi
    p = np.arctan(e * np.sin(E) / np.sqrt(1 - e **2))
    if i<13:
        p_degree = round((np.degrees(p) % 360),1)
    else:
        p_degree = round((np.degrees(p) % 360) - 360,1)

    return t, M_degree, E_degree, f_degree, r_c, v_c, p_degree

print("{:<12}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format("t-t0 (min)", "M (deg)", "E (deg)", "f (deg)", "r (km)", "v (km/s)", "Φ (deg)"))
for i in range(0, 25):
    t, M_degree, E_degree, f_degree, r_c, v_c, p_degree = calculate(i)
    print("{:<12}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format(t, M_degree, E_degree, f_degree, r_c, v_c, p_degree))
