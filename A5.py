import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt 
a =0
b =1
error = 1
accuracy = 1.0e-5

def f(x):
    return (x**(-1/4))/(math.e**x+x**(3/4)+2)
exact =quad(f,0,1)
def rectangle_mid_point (n) :
    h=(b-a)/n
    sums=0
    for i in range(n):
        sums +=f((a+h/2.0)+i*h)
    sums*=h
    return sums
#print(rectangle_mid_point(1000))
#0.3359595891868326
array_rect =[]
array_error =[]
init_number = 10
while(abs(error)>accuracy):
    array_rect.append(rectangle_mid_point(init_number))
    print(rectangle_mid_point(init_number))
    error =abs(rectangle_mid_point(init_number) - exact[0]) 
    print(error)
    array_error.append(error)
    init_number *=2
#0.33624197183356325 
# error 6.298654910419366e-06

def w(x): # w(x) from derivation shown in report
    return x**(-1/4)

def g(x):
    return 1/(math.e**x+x**(3/4)+2)

def F(x):
    return (3/4*x)**(4/3)

N = 1000
N_array = np.zeros(N)
sums = 0
sums_array =np.zeros(N)
x_total = np.zeros(N)
z_total = np.zeros(N)
for i in range(N):
    N_array[i] =i
    z = np.random.random()*4/3
    z_total[i] = z
    xi = F(z)
    x_total[i] = xi
    sums += g(xi)
    sums_array[i] =sums

plt.hist(x_total, bins = 100)
plt.title('non-uniform random number')
plt.scatter(N_array,z_total,linestyle ="dotted")
plt.plot(N_array,sums_array,linestyle ="dotted")
plt.show()
answer = (4/3)*(sums/N)
print(answer)
#0.3357569239874304
exact =quad(f,0,1)
print(exact)
#(0.33624827048847367, 2.93649216054348e-10)

#mean value method

a =0
b =1
sample_num =10000
size_samlpe = 10000
N_array = np.zeros(size_samlpe)
sums_array = np.zeros(size_samlpe)
mean_array = np.zeros(size_samlpe)
for i in range(sample_num):
    sums = 0
    N_array[i] =i
    for j in range(size_samlpe):
        xi = np.random.random()
        sums+= f(xi)
    mean_array[i] = (b-a)*sums/size_samlpe
print(mean_array)
plt.plot(N_array,mean_array,"*")
plt.title('ordinary mean value method')
plt.show()

plt.hist(mean_array, bins = 100)
plt.title('histogram using ordinary mean value method')
plt.show()

#mean value method using importance sampling 
sample_num =10000
size_samlpe = 10000
N_array = np.zeros(size_samlpe)
sums_array = np.zeros(size_samlpe)
mean_array = np.zeros(size_samlpe)
x_total = np.zeros(size_samlpe)
z_total = np.zeros(size_samlpe)
a =0
b =1
for i in range(sample_num):
    sums = 0
    N_array[i] =i
    for j in range(size_samlpe):
        z = np.random.random()*4/3
        z_total[i] = z
        xi = F(z)
        x_total[i] = xi
        sums += g(xi)
        sums_array[i] =sums
    mean_array[i] = (4/3)*sums/size_samlpe
plt.plot(N_array,mean_array,"*")
plt.title('mean value method with importance sampling')
plt.show()
plt.hist(mean_array, bins = 100)
plt.title('histogram using mean value method with importance sampling')
plt.show()

#MCMC
x_0 = np.random.random()
sample_num =10000
size_samlpe = 10000
sums_array = np.zeros(size_samlpe)
N_array = np.zeros(size_samlpe)
x_total = np.zeros(size_samlpe)
g_array = np.zeros(size_samlpe)
g_mean = np.zeros(size_samlpe)

for i in range(sample_num):
    sum_0 = 0
    for j in range(size_samlpe):
        x_1 = np.random.random()
        if(w(x_1)/w(x_0) > np.random.random()):
            x_total[i] = x_1
        else:
            x_total[i] = x_0
        x_0 = x_total[i]
        sum_0 += g(x_0)
    sums_array[i] = sum_0/size_samlpe*4/3
ans_mean = np.mean(sums_array)
#0.33624191817637156
error = (np.var(sums_array))
#8.397094460069438e-07
