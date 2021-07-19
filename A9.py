import numpy as np
import matplotlib.pyplot as plt
import math

# c = 1
# c_array = np.arange(0,2,0.01)

# x0 = 2
# accuracy = 10**(-8)
# error = 1
# #print(c_array)
# def h(c,x):
#     return 1 - math.e**(-c*x)+0.2*x

# def f(x):
#     return np.sqrt(1-math.log10(x))

# def g(x):
#     return x 

# x1_array =[]
# for i in range(len(c_array)):
#     error = 1
#     x0 = 2
#     while (error > accuracy):
#         c = c_array[i]
#         x1 = h(c, x0)
#         error  = abs(x1-x0)
#         x0  = x1
#     x1_array.append(x1)
# print(x1_array)
# print(len(c_array))
# plt.plot(c_array,x1_array,linestyle ='dotted')
# plt.xlabel("value of c")
# plt.ylabel("value of x")
# plt.show()

# using newton's method
G = 6.674*10**(-11)
M = 5.974*10**24
m = 7.348*10**22
R = 3.844*10**8
w = 2.662*10**-6
def Lagrange(r):
    return (G*M)/(r**2)-(G*m)/(R-r)**2-w**2*r
def DLagrange(r):
    return (-2*G*M)/(r**3)-(-2*-1*G*m)/(R-r)**3-w**2

r0 =3*10**4 #inital guess
error = 1
accu = 10**-6
while(error>accu):
    r1 = r0-Lagrange(r0)/DLagrange(r0)
    error = abs(r1-r0)
    r0 = r1
#print(r1) #326045071.66535544

# using secant method 
def Lagrange(r):
    return (G*M)/(r**2)-(G*m)/(R-r)**2-w**2*r
r0 = 3*10**5
r1 = 3*10**6
error = 1
accu = 10**-6
while(error>accu):
    r2 = r1-Lagrange(r1)*(r1-r0)/(Lagrange(r1)-Lagrange(r0))
    error = abs(r2-r1)
    r0 = r1
    r1 = r2
print(r2) #326045071.66535544