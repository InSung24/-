import numpy as np
import math

ti = [1.0,0.0,0.0]
tj = [0.0,1.0,0.0]
tk = [0.0,0.0,1.0]
r_v = [5492.00034, 3984.00140, 2.95581]
v_v = [-3.9310465491, 5.498676921, 3.665980697]

mu = 398600.5

def vts (vector):
    vts_sum = sum(coord ** 2 for coord in vector)
    vts_sq = math.sqrt(vts_sum)
    return vts_sq


def op (vector1, vector2):
    oproduct = [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]
    
    return oproduct

def ip (vector1,vector2):
    iproduct = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    return iproduct

# a
r_s = vts(r_v)
v_s = vts(v_v)
a = 1/((2/r_s) - (v_s*v_s/mu))

#e
h_v = op(r_v, v_v)
e_v = - (np.add(np.divide(r_v,r_s),np.divide(op(h_v,v_v),mu)))
e_s = vts(e_v)

#i
h_s = vts(h_v)
i = math.acos(ip(tk,h_v)/h_s)

#omm
n_v = op(tk,h_v)
n_s = vts(n_v)
omm = np.arctan2(ip(n_v, tj)/n_s, ip(n_v, ti)/n_s)

#omg
omg = np.arctan2((h_s*e_v[2])/(n_s*e_s), ip(n_v,e_v)/(n_s*e_s))
if (omg < 0):
    omg = omg + 2*np.pi


#f
f = np.arctan2(h_s*ip(r_v,v_v)/(mu*r_s*e_s), ip(r_v,e_v)/(r_s*e_s))


print("a : ", a, "\n")
print("e : ", e_s, "\n")
print("i : ", i * (180 / np.pi), "\n")
print("omm : ", omm * (180 / np.pi), "\n")
print("omg : ", omg * (180 / np.pi), "\n")
print("f : ", f * (180 / np.pi), "\n")   
