
import numpy as np
import matplotlib.pyplot as plt
import math

l = 0.01 # 1cm
m = 100
a = 1/m
accuracy = 10**(-6)
error = 1
iteration = 0
error_array = []
phi = np.zeros((m+1, m+1), float)
#phi[:,m] = 1 # boundary condition
phi[0,:] = 1

phi_new = np.zeros((m+1, m+1), float)
#phi_new[:,m] = 1
# no need to define rho because it is laplace equation 

max_iteration = 2000
while error>accuracy :
    if iteration< max_iteration:
        for i in range(m+1):
            for j in range(m+1):
                if (i == 0 or j ==0 or i == m or j == m):
                    phi_new[i,j] = phi[i,j]
                else:
                    phi_new[i,j] = (1/4) *(phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])
        error = np.max(abs(phi-phi_new))
        error_array.append(error)
        phi = phi_new # save the value of phi_new
        phi_new = np.zeros((m+1, m+1), float) #reset value of phi_new
        
    else:
        print("can not reach required accuracy within maximum iteration")
print(error_array)
plt.imshow(phi)
plt.colorbar()
plt.show()

# question 2 

l = 0.1
m = 100
a = 1/m
accuracy = 10**(-6)
error = 1
iteration = 0
error_array = []
phi = np.zeros((m+1, m+1), float)
# boundary condition
phi[0,:] = 0
phi[m,:] = 0
phi[:,0] = 0
phi[:,m] = 0
phi[20:80,20] = 1
phi[20:80,80] = -1

phi_new = np.zeros((m+1, m+1), float)
max_iteration = 2000
while error>accuracy :
    if iteration< max_iteration:
        for i in range(m+1):
            for j in range(m+1):
                if (i == 0 or j ==0 or i == m or j == m):
                    phi_new[i,j] = phi[i,j]
                elif(i >=20 and i < 80 and j == 20):
                    phi_new[i,j] = phi[i,j]
                elif(i >=20 and i < 80 and j == 80):
                    phi_new[i,j] = phi[i,j]
                else:
                    phi_new[i,j] = (1/4) *(phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])
        error = np.max(abs(phi-phi_new))
        error_array.append(error)
        phi = phi_new # save the value of phi_new
        phi_new = np.zeros((m+1, m+1), float) #reset value of phi_new
        
    else:
        print("can not reach required accuracy within maximum iteration")
print(error_array)
plt.imshow(phi)
plt.colorbar()
plt.show()