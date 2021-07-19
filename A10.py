import numpy as np
import matplotlib.pyplot as plt
import math

from numpy.lib.financial import _rate_dispatcher
a = 0.0
b = 2
N = 540           
H = (b-a)/N 
delta = 1000/52

theta0 = 0 
x0 = 0
#y0 = 1.4710*10**11
y0 = 4.4368*10**12
r_dis0 = math.sqrt(x0**2+y0**2)
#vx0 = 3.0287*10**4
vx0 = 6.1218*10**3
vy0 = 0
k = np.array([x0,y0,vx0,vy0],float)
G = 6.674*10**(-11)
M = 1.9891*10**30

def F(r,t):
    x = r[0]
    y = r[1]
    r_dis = math.sqrt(x**2+y**2)
    vx = r[2]
    vy = r[3]
    Fx = vx*t + x
    Fy = vy*t + y
    Fvx = (-1*G*M*x)/r_dis**3 
    Fvy = (-1*G*M*y)/r_dis**3 
    return np.array([Fx,Fy,Fvx,Fvy],float)
vx = H/2 * (-1*G*M*x0)/r_dis0**3
vx1 = vx0 + H * vx
x1 = x0 + vx1 * H
vy = H/2 * (-1*G*M*y0)/r_dis0**3
vy1 = vy0 + H * vy
y1 = y0 + vy1 * H
r1  =[x1, y1, vx1, vy1]
t= a
x_array = []
y_array = []
vx_array = []
vy_array = []
# x_array.append(r1[0])
# y_array.append(r1[1])
# vx_array.append(r1[2])
# vy_array.append(r1[3])
for i in range(N):
    
    r2 = k + H * F(r1,t+H/2)
    r1 = r1 + H * F(r2, t + H)
    r = r2
    t = t + H
    x_array.append(r[0])
    y_array.append(r[1])
    vx_array.append(r[2])
    vy_array.append(r[3])

print(x_array)
print(y_array)
plt.plot(x_array,y_array)
plt.show()

# for part 2 
x0 = 0
y0 = 4.4368*10**12
vx0 = 6.1218*10**3
vy0 = 0