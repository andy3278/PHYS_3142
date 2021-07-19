from numpy.lib.function_base import kaiser
from gaussxw import gaussxw
import numpy as np
import math
from scipy.integrate import dblquad
import matplotlib.pyplot as plt

a = -1*math.pi
b = math.pi
c = -1*math.pi
d = math.pi
kBT =1
N = 100

def f(kx,ky,kBT):
    return math.log(1+ math.exp(2*(math.cos(kx)+math.cos(ky))/kBT))

# points for x
x1,w1 = gaussxw(N)
xp1 = 0.5*(b-a)*x1+0.5*(b+a)
wp1 = 0.5*(b-a)*w1
#points for y
x2,w2 = gaussxw(N)
xp2 = 0.5*(d-c)*x2+0.5*(d+c)
wp2 = 0.5*(d-c)*w2

def free_energy():
    y = 0
    for i in range(N):
        for j in range(N):
            y += wp1[i]*wp2[j]*f(xp1[i],xp2[j],kBT)
    return -kBT*y
print(free_energy()) # value -42.63882030501868
#exact value using scipy (42.63882030501887, 1.2115732947751314e-07)
kBT_array = np.linspace(0.1,10,100)
free_energy_array = []
for i in range(N):
    kBT = kBT_array[i] # update kBT from 0.1 to 10
    free_energy_array.append(free_energy()) #append new data point
plt.plot(kBT_array,free_energy_array)
plt.xlabel("kBT")
plt.ylabel("F(T)")
plt.title('F(T) vs kBT')
plt.show()
t =1
k =1
A = np.array([[t,-2*math.cos(k)],[-2*math.cos(k),-t]])
band1 = []
band2 = []
k_array = np.linspace(-1*math.pi,math.pi,100)
e,v = np.linalg.eig(A)

print(e)
print(v)
for i in range(len(k_array)):
    k = k_array[i]
    A = np.array([[t,-2*math.cos(k)],[-2*math.cos(k),-t]])
    e,v = np.linalg.eig(A)
    band1.append(e[0])
    band2.append(e[1])
plt.plot(k_array,band1)
plt.plot(k_array,band2)
plt.legend(['epsilon_c','epsilon_d'])
plt.xlabel("epsilon")
plt.ylabel("k")
plt.title('epsilon vs k')
plt.show()

# h = 0.00001
# band1_with_h = []
# band2_with_h = []
# for i in range(len(k_array)):
#     k1 = k_array[i]+h
#     A1 = np.array([[t,-2*math.cos(k1)],[-2*math.cos(k1),-t]])
#     e1,v1 = np.linalg.eig(A1)
#     band1_with_h.append(e1[0])
#     band2_with_h.append(e1[1])
# group_v_1 = []
# group_v_2 = []
# for i in range(len(k_array)):
#     group_v_1.append((band1_with_h[i]-band1[i])/h)
#     group_v_2.append((band2_with_h[i]-band2[i])/h)
# plt.plot(k_array,group_v_1)
# plt.plot(k_array,group_v_2)
# plt.legend(['group_velocity_c','group_velocity_d'])
# plt.xlabel("group_velocity")
# plt.ylabel("k")
# plt.show()