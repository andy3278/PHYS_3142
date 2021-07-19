# %%
# Q1 Plot the d orbital angular wave function
import numpy as np
import matplotlib.pyplot as plt
import math
def dx2_y2_obrbital (x,y,z):
    r2=x**2+y**2+z**2 
    a0=1
    Rr=4/81/np.sqrt(30)*r2/a0/a0*np.exp(-r2/3/a0)
    if(r2 == 0):
        return 0
    return Rr*math.sqrt(15/4)*(x**2-y**2)/r2*math.sqrt(1/(4*math.pi))
x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)
z = 0
H = np.zeros((100,100),float)
for i in range(len(x)):
    for j in range(len(y)):
        H[i][j] = dx2_y2_obrbital(x[i], y[j], z)
plt.contourf(x,y,H)
plt.axis('square')
# %%
# Q2 Prime number
n = input('plsease input a number with at least 4 digits')
while(len(n) < 4):
    n = input('plsease input a number with at least 4 digits')
n = int(n) # turn n from string to integer
def check_prime (number):
    for i in range(2, number): 
        if(number % i == 0): # loop every number before the target check for prime 
            print("{}".format(number) +' is not a prime number')
            return False
            break
    print("{}".format(number) +' is a prime number') # if didnt find a number before target which means it is a prime number
    return True
import sympy
if(sympy.isprime(n) == check_prime(n)):
    print('answer correct!')
else :
    print('something is wrong...')
# input :131243432 
# output :131243432 is not a prime number answer correct!

# %%
# Q3 Draw the trajectories
import math
import numpy as np
import matplotlib.pyplot as plt
v1 = 100
g = 9.8
x_init = 0
y_init = 0
angle_1 = 30*math.pi/180
angle_2 = 45*math.pi/180
angle_3 = 60*math.pi/180
def y_motion_equation(angle,t):
    y_final = y_init +(v1*math.sin(angle)*t )-((g*t**2)/2)
    return y_final
def x_motion_equation(angle,t):
    x_final = x_init +v1*math.cos(angle)*t
    return x_final
time = np.linspace(0, 20, 100, endpoint=True)
height_angle_1 = []
height_angle_2 = []
height_angle_3 = []
range_angle_1 = []
range_angle_2 = []
range_angle_3 = []
for i in range(len(time)):
    height_angle_1.append(y_motion_equation(angle_1, time[i]))
for i in range(len(time)):
    height_angle_2.append(y_motion_equation(angle_2, time[i]))
for i in range(len(time)):
    height_angle_3.append(y_motion_equation(angle_3, time[i]))
for i in range(len(time)):
    range_angle_1.append(x_motion_equation(angle_1, time[i]))
for i in range(len(time)):
    range_angle_2.append(x_motion_equation(angle_2, time[i]))
for i in range(len(time)):
    range_angle_3.append(x_motion_equation(angle_3, time[i]))
plt.plot(range_angle_1,height_angle_1, 'r', marker = '.', linestyle='solid')
plt.plot(range_angle_2,height_angle_2, 'g', marker = '+', linestyle='dashdot')
plt.plot(range_angle_3,height_angle_3, 'b', marker = '*', linestyle='dotted')
plt.ylim(0)
plt.xlim(0,1100)
plt.legend(['30 degrees', '45 degrees', '60 degrees'])
plt.xlabel("Range (m)")
plt.ylabel("Height (m)")
plt.title('projectile motion with difference angles')
plt.show()
# %%
# Q4 Dictionary practice
Atomic_number = {
    "Au" : 79,
    "Cu" : 29,
    "Fe" : 26,
    "Ag" : 47,
    "Zn" : 30
}
Melting_point = {
    "Au" : 1064,
    "Cu" : 1085,
    "Fe" : 1538,
    "Ag" : 961,
    "Zn" : 419
}
Density = {
    "Au" : 19.3,
    "Cu" : 8.96,
    "Fe" : 7.87,
    "Ag" : 10.49,
    "Zn" : 7.13
}
# Q5 Bubble Sort 
def sort_descnding_order (list):
    for i in range(len(list)-1):
        for j in range(0,len(list)-i-1):
            if(list[j] < list[j+1]):
                temp = list[j] # if condition met, store the data in temp
                list[j] = list[j+1] # swap the position
                list[j+1] = temp
    return list
Atomic_number_list = list(Atomic_number.values()) # converting dictionary to list
Melting_point_list = list(Melting_point.values())
Density_list = list(Density.values())
print(sort_descnding_order(Atomic_number_list)) # [79, 47, 30, 29, 26]
print(sort_descnding_order(Melting_point_list)) # [1538, 1085, 1064, 961, 419]
print(sort_descnding_order(Density_list)) # [19.3, 10.49, 8.96, 7.87, 7.13]
# %%

# %%
