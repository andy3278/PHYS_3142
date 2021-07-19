import numpy as np
import matplotlib.pyplot as plt
import math

D = 6.9*10**-11

T_init = 1400
L = 0.05 #5cm 
N = 100
a = L/N
T = np.empty(N+1, float)
T[0] = T_init
T_new =np.empty(N+1, float)
h = 10 # time step is 10 second
concentration = np.empty(N+1, float)
concentration[0] = 0
concentration[N] = 0
concentration[1:N] = 0.2
concentration_new = np.empty(N+1, float)
t = 0
t0 = 20*3600
t1 = 40*3600
t2 = 60*3600
thickness  = np.arange(0,L+a,a)
#print(len(thickness))
# initial condition for alloy C(x,0) = 0.2
# C(0.05,t) = 0
# inital condition for air C(0,t) = 0
# T(t=0) = 1400

while t< t0 :
    for i in range(N+1):
        if(i==0 or i ==N):
            concentration_new[i] = concentration[i]
        else:
            concentration_new[i] = concentration[i] + h*D/a**2*(concentration[i+1]+concentration[i-1]-2*concentration[i])
    concentration = concentration_new # update 
    concentration_new = np.empty(N+1, float) # reset 
    t += h # increase time 
concentration_new1 = np.empty(N+1, float)
while t< t1 :
    for i in range(N+1):
        if(i==0 or i ==N):
            concentration_new1[i] = concentration[i]
        else:
            concentration_new1[i] = concentration[i] + h*D/a**2*(concentration[i+1]+concentration[i-1]-2*concentration[i])
    concentration = concentration_new1 # update 
    concentration_new1 = np.empty(N+1, float) # reset 
    t += h
concentration_new2 = np.empty(N+1, float)
while t< t2 :
    for i in range(N+1):
        if(i==0 or i ==N):
            concentration_new2[i] = concentration[i]
        else:
            concentration_new2[i] = concentration[i] + h*D/a**2*(concentration[i+1]+concentration[i-1]-2*concentration[i])
    concentration = concentration_new2 # update 
    concentration_new2 = np.empty(N+1, float) # reset 
    t += h
plt.plot(thickness,concentration_new,label = "20 hours")
plt.plot(thickness,concentration_new1,label = "40 hours")
plt.plot(thickness,concentration_new2,label = "60 hours")
plt.xlabel("thickness (m)")
plt.ylabel("concentration")
plt.title("concentration of carbon versus thickness of the alloy")
plt.legend()
plt.show()
print(len(concentration_new))
while max(concentration)> 0.05 :
    for i in range(N+1):
        if(i==0 or i ==N):
            concentration_new[i] = concentration[i]
        else:
            concentration_new[i] = concentration[i] + h*D/a**2*(concentration[i+1]+concentration[i-1]-2*concentration[i])
    concentration = concentration_new # update 
    concentration_new = np.empty(N+1, float) # reset 
    t += h
print(t) 
# time needed for 5% concentration everywhere is 5976150 seconds which is around 69 days
