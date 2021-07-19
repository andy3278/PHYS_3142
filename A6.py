import numpy as np
import matplotlib.pyplot as plt
nx = 10
ny = 10
J_ = 2
T0 = 1
T1 = 20
kB = 1

latt = np.zeros((nx,ny))
for i in range(nx):
    for j in range(ny):
        a = np.sign(np.random.random()-0.5)
        latt[i, j] = a

def H(i,j):
    H = -1*latt[i,j]*J_*((latt[i,np.mod(j+1,ny)]+ latt[i, np.mod(j-1, ny)])\
                    +(latt[np.mod(i + 1, nx),j] + latt[np.mod(i-1, nx), j])) # use mod to bound the input
    return H

def delta_H(i,j):
    H_ = -2 * H(i,j)
    return H_

T = np.arange(T0, T1, 0.2)
Num_sample = 100
num_filp = 5
total_M = np.zeros((len(T),Num_sample*num_filp))
final_M = np.zeros(len(T))
total_H = np.zeros((len(T),Num_sample*num_filp))
final_H = np.zeros(len(T))
final_Susceptibility = np.zeros(len(T))
final_Heat_capacity = np.zeros(len(T))
xx = 0

for t in T:
    yy = 0
    for i in range(Num_sample):
        for j in range(num_filp):
            for m in range(nx * ny):
                x = np.random.randint(nx)
                y = np.random.randint(ny)
                if min(1, np.exp(-delta_H(x,y)/t))>np.random.random():
                    latt[x,y] = -latt[x,y]
            total_H[xx,yy] = np.sum(np.sum(H(np.mod(i,nx),np.mod(j,ny)))) # use mod to bound the input
            total_M[xx,yy] = np.sum(np.sum(latt))/nx/ny 
            yy += 1
    
    final_M[xx] = np.mean(total_M[xx,:]) #save mean value of numebr xx row to a list
    final_H[xx] = np.mean(total_H[xx,:]) #save mean value of numebr xx row to a list
    final_Susceptibility[xx] = (np.mean(total_M[xx,:]**2)-np.mean(total_M[xx,:])**2)/t
    final_Heat_capacity[xx] = (np.mean(total_H[xx,:]**2)-np.mean(total_H[xx,:])**2)/(kB*t**2)
    xx +=1

plt.plot(T,final_H,linestyle ='dotted')
plt.title('Energy vs time')
plt.show()
plt.plot(T,final_M,linestyle ='dotted')
plt.title('Magnetization vs time')
plt.show()
plt.plot(T,final_Heat_capacity,linestyle ='dotted')
plt.title('Heatcapacity vs time')
plt.show()
plt.plot(T,final_Susceptibility,linestyle ='dotted')
plt.title('Susceptibility vs time')
plt.show()

# %%
s = [1,2,3,4,4.1,5,6,7]
s1 = s[3:-3]
print(s1)
# %%
