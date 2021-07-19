import numpy as np
import time as time
from numpy import copy


def banded(Aa,va,up,down):
    t0 = time.time()
    A = copy(Aa)*1.0
    v = copy(va)*1.0
    N = len(v)
    # Gaussian elimination
    for m in range(N):
        # Normalization factor
        div = A[up,m]
        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]

        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]

    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]
    t1 = time.time()
    t_final = t1-t0
    return v, t_final


def create_A(N):
    a = np.zeros((N,N),float)
    a[0,0] = 3
    a[-1,-1] = 3
    for i in range(N):
        for j in range(N):
            if(i==j and (i ==0 or i ==N-1)):
                a[i,j] = 3
            elif(i==j):
                a[i,j] =4
            else:
                a[i,j] =-1
    return a
def create_w(N):
    a=np.zeros(N,float)
    for i in range(N):
        if( i ==0 or i ==1):
            a[i] = 1
        else:
            a[i] = 0
    return a
# print(create_A(5))
A = create_A(5)
w = create_w(5)
# x = np.linalg.solve(A, w)
# print(x)
# #[-0.875 -0.7   -0.9   -0.9   -1.125]
# A = create_A(6)
# w = create_w(6)
# x = np.linalg.solve(A, w)
# print(x)
#[-0.125 -0.1   -0.3   -0.3   -0.3   -0.375]
# t0_linalg = time.time()
# A = create_A(10000)
# w = create_w(10000)
# x = np.linalg.solve(A, w)
# t1_linalg = time.time()
# time_linalg = t1_linalg-t0_linalg
# print(time_linalg)
#28.2967631816864
print(banded(A,w,2,2))