# %%
import math
from numpy.lib.function_base import extract
from scipy.integrate import quad
import matplotlib.pyplot as plt
from gaussxw import gaussxw, gaussxwab
import math
from scipy.integrate import quad
def f(x):
    
    return ((math.sin(x)+3*math.cos(x)-3)/math.sqrt(x) )+4
b=1
a=0.000001
error =1
accuracy = 1.0e-5
exact =quad(f,0,1)
#4.047682030848447
def rectangle_mid_point (n) :
    h=(b-a)/n
    sums=0
    for i in range(n):
        sums +=f((a+h/2.0)+i*h)
    sums*=h
    return sums
print(rectangle_mid_point(320))
array_rect =[]
array_error =[]
init_number = 10
# while(abs(error)>accuracy):
#     array_rect.append(rectangle_mid_point(init_number))
#     print(rectangle_mid_point(init_number))
#     error =abs(rectangle_mid_point(init_number) - exact[0]) 
#     print(error)
#     array_error.append(error)
#     init_number *=2

# %%
def trapezoidal(n):
    h=(b-a)/n
    sums= (f(b)+f(a))/2.0
    for i in range(1,n):
        sums += f(a + i*h)
    sums *= h
    return sums
def adaptive_second(num_slice):
    h=(b-a)/num_slice
    sums=0
    for i in range(1,num_slice,2):
        sums += f(a+i*h)
    
    sums *= h
    return sums

NN=10
tpz_sum=trapezoidal(NN)
print("N=","%6s"%str(NN)," ,Error=","%g" %(error))
tpz_sum_old=tpz_sum
while abs(error)>accuracy:
    NN=NN*2
    tpz_sum=tpz_sum_old/2.0 + adaptive_second(NN)  
    error = abs((tpz_sum-tpz_sum_old)/3.0)  
    tpz_sum_old=tpz_sum
    
    print("N=","%6s"%str(NN),", Error=","%.5g" %(error))
# I =quad(f,0,1)
# print(I)
# %%
def Simpson(n):
    h=(b-a)/n
    sums =f(a)+f(b)
    even =0
    odd =0
    for i in range(1,n/2):
        even += f(a+(2*i-1)*h)
    sums =sums + 4*even
    for i in range(1,(n/2-1)):
        odd += f(a+2*i*h)
    sums = sums+ 2*odd
    return sums*h/3.0

print(Simpson(100))
# %%
from gaussxw import gaussxw, gaussxwab
import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
def f(x):
    return ((math.sin(x)+3*math.cos(x)-3)/math.sqrt(x))+4
b=1
a=0
error =1
accuracy = 1.0e-5
exact =quad(f,0,1)
array_error =[]
array_num =[]
N =3
while (abs(error) > accuracy):
    x,w = gaussxwab(N,a,b)
    sums =0
    for i in range(N):
        sums = sums+ w[i] *f(x[i])
    array_num.append(N)
    N +=2
    error =abs(sums - exact[0])
    array_error.append(error)
    print(N)
    print(error)
    print(sums)
plt.plot(array_num,array_error,'r', marker = '.', linestyle='solid')
plt.xlabel("number of points")
plt.ylabel("error")
plt.title('Gauss')
plt.show()
# %%
