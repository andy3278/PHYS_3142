import numpy as np
import matplotlib.pyplot as plt
vaccine_group = 21720
placebo_group = 21728
vaccine_postive = 8
placebo_postive = 162
vaccine_suspected = 1594
placebo_suspected = 1816
def VE (alpha):
    placebo_num = (placebo_postive+ alpha*placebo_suspected)/placebo_group
    vaccine_num = (vaccine_postive+alpha*vaccine_suspected)/vaccine_group
    return (placebo_num-vaccine_num)*100/placebo_num

alpha_array = np.linspace(0,0.5,100)
VE_array = []
for i in range(len(alpha_array)):
    VE_array.append(VE(alpha_array[i]))
plt.plot(alpha_array,VE_array)
plt.xlabel("false negative rate alpha")
plt.ylabel("Vaccine Efficacy (%)")
plt.title('Vaccine Efficacy as function of false negative rate')
plt.show()


import numpy as np
import math

NN = 10000 # number of sample
N = 1000 # ponits for sample
count_sphere =0
count_cylinder = 0
count_both =0
V_total = np.zeros(NN)
for i in range(NN):
    for j in range(N):
        x = 2*np.random.random()-1
        y = 2*np.random.random()-1
        z = 2*np.random.random()-1
        r_shpere = x**2 +y**2 +z**2
        r_cylinder = (x-0.5)**2 +y**2
        if(r_shpere<1):
            count_sphere +=1
        if(r_cylinder<0.25):
            count_cylinder +=1
        if(r_shpere<1 and r_cylinder<0.25):
            count_both +=1
    V = math.pi/2*count_both/count_cylinder
    V_total[i] = V
V_mean = np.sum(V_total)/NN
uncertainty = 0
for i in range(NN):
    uncertainty += 1/(NN-1)*(V_total[i]-V_mean)**2
print(V_mean)
print(uncertainty)
#1.204883013992805
#9.62887081300469e-07

