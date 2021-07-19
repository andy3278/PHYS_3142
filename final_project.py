#question 1
import numpy as np
import matplotlib.pyplot as plt
import math

G = 6.6738*10**(-11)
M_sun = 1.9891*10**(30)
M_earth = 1.9891*10**(30)
M_pluto = 1.9891*10**(30)

# intial conditions for the earth
vx0_e = 3.0287 * 10 **4
vy0_e = 0
y0_e = 1.4710 * 10**11
x0_e = 0
# intial conditions for the pluto
vx0_p = 6.1218 * 10 **3
vy0_p = 0
y0_p = 4.4368 * 10 **12
x0_p = 0

# intial conditions for the sun
vx0_s = 0
vy0_s = 0
y0_s = 0
x0_s = 0

position_x_e = []
position_y_e = []

position_x_p = []
position_y_p = []

position_x_s = []
position_y_s = []

a = 0
b = 1 * 365 * 24 * 60 * 60 
b2 = 250 * b
accuracy = 1000 / 365/24/60/60
H = 7 * 24 * 60 * 60
t = 0
dt = H

# %%

while t < 2*b:
    # r = aerth - sun
    rx =  x0_e - x0_s
    ry =  y0_e - y0_s
    #rz =  z0_e - z0_s

    r_dis = math.sqrt(rx**2+ry**2)
    fx = -G * M_sun * M_earth * rx/(r_dis**3)
    fy = -G * M_sun * M_earth * ry/(r_dis**3)
    #fx = -G * rx/(r_dis**3)
    # update vilocity and position of earth
    vx0_e += fx*dt/M_earth
    vy0_e += fy*dt/M_earth
    x0_e += vx0_e*dt
    y0_e += vy0_e*dt
    position_x_e.append(x0_e)
    position_y_e.append(y0_e)
    # update vilocity and position of sun
    vx0_s += -fx*dt/M_sun
    vy0_s += -fy*dt/M_sun
    x0_s += vx0_s*dt
    y0_s += vy0_s*dt
    position_x_s.append(x0_s)
    position_y_s.append(y0_s)

    t += dt

# print(position_x_s,position_y_s)
# print(position_x_e,position_y_e)
plt.plot(position_x_e,position_y_e,color ="b")
plt.plot(position_x_s,position_y_s, color = "r")
plt.title('Earth and sun two body problem')
plt.legend(['earth','sun'])
plt.show()

# intial conditions for the pluto
vx0_p = 6.1218 * 10 **3
vy0_p = 0
y0_p = 4.4368 * 10 **12
x0_p = 0

# intial conditions for the sun
vx0_s = 0
vy0_s = 0
y0_s = 0
x0_s = 0

position_x_p = []
position_y_p = []

position_x_s = []
position_y_s = []

t = 0
dt = H
# for another inital condition
while t < b2:
    # r = pluto - sun
    rx =  x0_p - x0_s
    ry =  y0_p - y0_s
    #rz =  z0_e - z0_s

    r_dis = math.sqrt(rx**2+ry**2)
    fx = -G * M_sun * M_pluto * rx/(r_dis**3)
    fy = -G * M_sun * M_pluto * ry/(r_dis**3)
    #fx = -G * rx/(r_dis**3)
    # update vilocity and position of pluto
    vx0_p += fx*dt/M_pluto
    vy0_p += fy*dt/M_pluto
    x0_p += vx0_p*dt
    y0_p += vy0_p*dt
    position_x_p.append(x0_p)
    position_y_p.append(y0_p)
    # update vilocity and position of sun
    vx0_s += -fx*dt/M_sun
    vy0_s += -fy*dt/M_sun
    x0_s += vx0_s*dt
    y0_s += vy0_s*dt
    position_x_s.append(x0_s)
    position_y_s.append(y0_s)

    t += dt

plt.plot(position_x_p,position_y_p,color ="c")
plt.plot(position_x_s,position_y_s, color = "r")
plt.title('pluto and sun two body problem')
plt.legend(['pluto','sun'])
plt.show()

# question 2
M_sun1 = 5*1.9891*10**(30)
M_sun2 = 5*1.9891*10**(30)
M_sun3 = 5*1.9891*10**(30)
M_earth = 5.972*10**(24)
G = 6.6738*10**(-11)
position_x_s1 = []
position_y_s1 = []
position_x_s2 = []
position_y_s2 = []
position_x_s3 = []
position_y_s3 = []
position_x_e = []
position_y_e = []
# first set of inital condition\
# init_s1 = [2*10**2,5*10**3,0,0]
# init_s2 = [8.5675*10**4,0,4.4368*10**12,3.5335*10**6] 
# init_s3 = [9.4353*10**2,1.3232*10**2,6.3453*10**7,2.5353*10**5]
# second set of inital condition\
# init_s1 = [-2*10**1,-2.5*10**2,6.3453*10**12,6.3453*10**12]
# init_s2 = [-8.5675*10**2,3.5675*10**1,-4.4368*10**12,4.4368*10**12] 
# init_s3 = [3.4353*10**1,1.3232*10**3,-2.5353*10**12,-2.5353*10**12]
# thrid set of inital condition\
# init_s1 = [3.0287 * 10 **2, -4.3232 *10**1 ,1.4710 * 10 **11,0]
# init_s2 = [8.5675*10**4,0,4.4368*10**12,3.5335*10**6] 
# init_s3 = [9.4353*10**2,1.3232*10**2,6.3453*10**7,2.5353*10**5]
vx0_s1 = -1.44*2*0**1
vy0_s1 = -29789*10**3
y0_s1 = 0.5*6.3453*0**12
x0_s1 = -2*10**12
vx0_s2 = -8.5675*0**2
vy0_s2 = 29789*10**3
y0_s2 = -4.4368*0**12
x0_s2 = 2*10**12
vx0_s3 = 3.4353*0**1
vy0_s3 = 44684*10**3
y0_s3 = -2.5353*0**12
x0_s3 = 8*10**12
vx0_e = 1.9*3.0287 * 10 **2
vy0_e = -4.3232 *10**1
y0_e = 1.77*1.4710 * 10 **11
x0_e = -2.5353 * 10 **11

a = 0
b = 1 * 365 * 24 * 60 * 60 
b2 = 250 * b
accuracy = 1000 / 365/24/60/60
H = 1 * 24 * 60 * 60
t = 0
dt = H
# def threebody(r1,r2,r3):
#     rx_12 = r1[3]-r2[3]
#     rx_13 = r1[3]-r3[3]
#     rx_23 = r2[3]-r3[3]
#     ry_12 = r1[2]-r2[2]
#     ry_13 = r1[2]-r3[2]
#     ry_23 = r2[2]-r3[2]
#     r_dis_12 = math.sqrt(rx_12**2+ry_12**2)
#     r_dis_13 = math.sqrt(rx_13**2+ry_13**2)
#     r_dis_23 = math.sqrt(rx_23**2+ry_23**2)
#     R = [rx_12,rx_13,rx_23,ry_12,ry_13,ry_23,r_dis_12,r_dis_13,r_dis_23]
#     return R
# def r(rx,ry):
#     return rx-ry
# def rad(rx,ry):
#     return math.sqrt(rx_e1**2+ry_e1**2)
# def f(m1,m2,r,r_):
#     return -G * m1 * m2 * r/(r_**3)
while t < b2:
    # r_dis= threebody(init_s1,init_s2,init_s3)[-3:]
    # rx = threebody(init_s1,init_s2,init_s3)[:-6]
    # ry = threebody(init_s1,init_s2,init_s3)[3:-3]
    rx_12 = x0_s1 -x0_s2
    rx_13 = x0_s1 -x0_s3
    rx_23 = x0_s2 -x0_s3
    ry_12 = y0_s1 -y0_s2
    ry_13 = y0_s1 -y0_s3
    ry_23 = y0_s2 -y0_s3

    rx_e1 = x0_e - x0_s1
    rx_e2 = x0_e - x0_s2
    rx_e3 = x0_e - x0_s3
    ry_e1 = y0_e - y0_s1
    ry_e2 = y0_e - y0_s2
    ry_e3 = y0_e - y0_s3

    r_dis_e1 = math.sqrt(rx_e1**2 + ry_e1**2)
    r_dis_e2 = math.sqrt(rx_e2**2 + ry_e2**2)
    r_dis_e3 = math.sqrt(rx_e3**2 + ry_e3**2)
    fx_e1 = -G* M_earth * M_sun1 * rx_e1/(r_dis_e1)**3
    fy_e1 = -G* M_earth * M_sun1 * ry_e1/(r_dis_e1)**3
    fx_e2 = -G* M_earth * M_sun2 * rx_e2/(r_dis_e2)**3
    fy_e2 = -G* M_earth * M_sun2 * ry_e2/(r_dis_e2)**3
    fx_e3 = -G* M_earth * M_sun3 * rx_e3/(r_dis_e3)**3
    fy_e3 = -G* M_earth * M_sun3 * ry_e3/(r_dis_e3)**3
    vx0_e += (fx_e1 + fx_e2 + fx_e3)*dt/M_earth
    vy0_e += (fy_e1 + fy_e2 + fy_e3)*dt/M_earth
    

    x0_e += vx0_e*dt
    y0_e += vy0_e*dt

    position_x_e.append(x0_e)
    position_y_e.append(y0_e)

    r_dis_12 = math.sqrt(rx_12**2 + ry_12**2)
    r_dis_13 = math.sqrt(rx_13**2 + ry_13**2)
    r_dis_23 = math.sqrt(rx_23**2 + ry_23**2)
    fx_12 = -G* M_sun1 * M_sun2 * rx_12 / (r_dis_12)**3
    fy_12 = -G* M_sun1 * M_sun2 * ry_12 / (r_dis_12)**3
    fx_13 = -G* M_sun1 * M_sun3 * rx_13 / (r_dis_13)**3
    fy_13 = -G* M_sun1 * M_sun3 * ry_13 / (r_dis_13)**3
    fx_23 = -G* M_sun2 * M_sun3 * rx_23 / (r_dis_23)**3
    fy_23 = -G* M_sun2 * M_sun3 * ry_23 / (r_dis_23)**3
    # update the value of velocity 
    vx0_s1 += (fx_12 + fx_13)*dt/M_sun1
    vy0_s1 += (fy_12 + fy_13)*dt/M_sun1
    vx0_s2 += (-fx_12 + fx_23)*dt/M_sun2
    vy0_s2 += (-fy_12 + fy_23)*dt/M_sun2
    vx0_s3 += (-fx_13 + -fx_23)*dt/M_sun3
    vy0_s3 += (-fy_13 + -fy_23)*dt/M_sun3

    x0_s1 += vx0_s1*dt
    y0_s1 += vy0_s1*dt
    x0_s2 += vx0_s2*dt
    y0_s2 += vy0_s2*dt
    x0_s3 += vx0_s3*dt
    y0_s3 += vy0_s3*dt
    position_x_s1.append(x0_s1)
    position_y_s1.append(y0_s1)
    position_x_s2.append(x0_s2)
    position_y_s2.append(y0_s2)
    position_x_s3.append(x0_s3)
    position_y_s3.append(y0_s3)
    t += dt

plt.plot(position_x_s1,position_y_s1,color ="r")
plt.plot(position_x_s2,position_y_s2,color ="m")
plt.plot(position_x_s3,position_y_s3,color ="y")
plt.plot(position_x_e,position_y_e,color = "b")
plt.title('earth and three sun body problem')
plt.legend(['sun1','sun2','sun3','earth'])
plt.show()


# question 3
G = 6.6738*10**(-11)
M_sun = 1.9891*10**(30)

# intial conditions for the earth
vx0_e = 30038.588
vy0_e = 0
vz0_e = 0
y0_e = 1.4708 * 10**11
x0_e = 0
z0_e = 0
# intial conditions for the Mercury
vx0_M = 53711.756
vy0_M = 0
vz0_M = 0
y0_M = 4.60017*10**10
x0_M = 0
z0_M = 0

# initial conditions for Venus
vx0_v = 35140.627
vy0_v = 0
vz0_v = 0
y0_v = 1.0747158*10**11
x0_v = 0
z0_v = 0

# initial conditions for Mars
vx0_ma = 25340.2493
vy0_ma = 0
vz0_ma = 0
y0_ma = 2.066764*10**11
x0_ma = 0
z0_ma = 0

# initial conditions for Jupiter
vx0_j = 13312.576
vy0_j = 0
vz0_j = 0
y0_j = 7.408839*10**11
x0_j = 0
z0_j = 0

# intial conditions for the sun 
vx0_s = 0
vy0_s = 0
vz0_s = 1*10**3
y0_s = 0
x0_s = 0
z0_s = 0

position_x_e = []
position_y_e = []
position_z_e = []

position_x_M = []
position_y_M = []
position_z_M = []

position_x_v = []
position_y_v = []
position_z_v = []

position_x_ma = []
position_y_ma = []
position_z_ma = []

position_x_j = []
position_y_j = []
position_z_j = []

position_x_s = []
position_y_s = []
position_z_s = []
a = 0
b = 1 * 365 * 24 * 60 * 60 
b2 = 250 * b
accuracy = 1000 / 365/24/60/60
H = 7 * 24 * 60 * 60
t = 0
dt = H

while t < 6*b:
    # r = aerth - sun
    rx_es =  x0_e - x0_s
    ry_es =  y0_e - y0_s
    rz_es = z0_e - z0_s
    
    rx_Ms = x0_M - x0_s
    ry_Ms = y0_M - y0_s
    rz_Ms = z0_M - z0_s

    rx_vs = x0_v - x0_s
    ry_vs = y0_v - y0_s
    rz_vs = z0_v - z0_s

    rx_mas = x0_ma - x0_s
    ry_mas = y0_ma - y0_s
    rz_mas = z0_ma - z0_s

    rx_js = x0_j - x0_s
    ry_js = y0_j - y0_s
    rz_js = z0_j - z0_s

    r_dis_es = math.sqrt(rx_es**2+ry_es**2+rz_es**2)
    fx_e = -G * M_sun * rx_es/(r_dis_es**3)
    fy_e = -G * M_sun * ry_es/(r_dis_es**3)
    fz_e = -G * M_sun * rz_es/(r_dis_es**3)

    r_dis_Ms = math.sqrt(rx_Ms**2+ry_Ms**2+rz_Ms**2)
    fx_M = -G * M_sun * rx_Ms/(r_dis_Ms**3)
    fy_M = -G * M_sun * ry_Ms/(r_dis_Ms**3)
    fz_M = -G * M_sun * rz_Ms/(r_dis_Ms**3)

    r_dis_vs = math.sqrt(rx_vs**2+ry_vs**2+rz_vs**2)
    fx_v = -G * M_sun * rx_vs/(r_dis_vs**3)
    fy_v = -G * M_sun * ry_vs/(r_dis_vs**3)
    fz_v = -G * M_sun * rz_vs/(r_dis_vs**3)

    r_dis_mas = math.sqrt(rx_mas**2+ry_mas**2+rz_mas**2)
    fx_ma = -G * M_sun * rx_mas/(r_dis_mas**3)
    fy_ma = -G * M_sun * ry_mas/(r_dis_mas**3)
    fz_ma = -G * M_sun * rz_mas/(r_dis_mas**3)

    r_dis_js = math.sqrt(rx_js**2+ry_js**2+rz_js**2)
    fx_j = -G * M_sun * rx_js/(r_dis_js**3)
    fy_j = -G * M_sun * ry_js/(r_dis_js**3)
    fz_j = -G * M_sun * rz_js/(r_dis_js**3)

    # update vilocity and position of earth
    vx0_e += fx_e*dt
    vy0_e += fy_e*dt
    vz0_e += fz_e*dt
    x0_e += vx0_e*dt
    y0_e += vy0_e*dt
    z0_e += vz0_e*dt
    position_x_e.append(x0_e)
    position_y_e.append(y0_e)
    position_z_e.append(z0_e)
    # update Mercury
    vx0_M += fx_M*dt
    vy0_M += fy_M*dt
    vz0_M += fz_M*dt
    x0_M+= vx0_M*dt
    y0_M+= vy0_M*dt
    z0_M+= vz0_M*dt
    position_x_M.append(x0_M)
    position_y_M.append(y0_M)
    position_z_M.append(z0_M)
    #update Venus
    vx0_v += fx_v*dt
    vy0_v += fy_v*dt
    vz0_v += fz_v*dt
    x0_v+= vx0_v*dt
    y0_v+= vy0_v*dt
    z0_v+= vz0_v*dt
    position_x_v.append(x0_v)
    position_y_v.append(y0_v)
    position_z_v.append(z0_v)
    #update Mars
    vx0_ma += fx_ma*dt
    vy0_ma += fy_ma*dt
    vz0_ma += fz_ma*dt
    x0_ma+= vx0_ma*dt
    y0_ma+= vy0_ma*dt
    z0_ma+= vz0_ma*dt
    position_x_ma.append(x0_ma)
    position_y_ma.append(y0_ma)
    position_z_ma.append(z0_ma)
    #update Jupiter
    vx0_j += fx_j*dt
    vy0_j += fy_j*dt
    vz0_j += fz_j*dt
    x0_j+= vx0_j*dt
    y0_j+= vy0_j*dt
    z0_j+= vz0_j*dt
    position_x_j.append(x0_j)
    position_y_j.append(y0_j)
    position_z_j.append(z0_j)
    # update vilocity and position of sun
    z0_s += vz0_s*dt
    position_x_s.append(x0_s)
    position_y_s.append(y0_s)
    position_z_s.append(z0_s)
    t += dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import mpl_toolkits.mplot3d.axes3d as p3
def func(num, data1,data2,data3,data4,data5,data6, line1,line2,line3,line4,line5,line6):
    # there is no .set_data() for 3 dim data...
    line1.set_data(data1[0:2, :num])    
    line1.set_3d_properties(data1[2, :num])
    line2.set_data(data2[0:2, :num])    
    line2.set_3d_properties(data2[2, :num]) 
    line3.set_data(data3[0:2, :num])    
    line3.set_3d_properties(data3[2, :num])
    line4.set_data(data4[0:2, :num])    
    line4.set_3d_properties(data4[2, :num])
    line5.set_data(data5[0:2, :num])    
    line5.set_3d_properties(data5[2, :num]) 
    line6.set_data(data6[0:2, :num])    
    line6.set_3d_properties(data6[2, :num])     
    return [line1,line2,line3,line4,line5,line6]

fig = plt.figure()
ax = p3.Axes3D(fig)
data1 = np.array([position_x_e,position_y_e,position_z_e])
data2 = np.array([position_x_s,position_y_s,position_z_s])
data3 = np.array([position_x_M,position_y_M,position_z_M])
data4 = np.array([position_x_v,position_y_v,position_z_v])
data5 = np.array([position_x_ma,position_y_ma,position_z_ma])
data6 = np.array([position_x_j,position_y_j,position_z_j])
num_data = len(position_x_e)
#print(data.shape)
#lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
line1 = plt.plot(data1[0],data1[1],data1[2],lw=2,color ="g")[0]
line2 = plt.plot(data2[0],data2[1],data2[2],lw=2, color = "r")[0]
line3 = plt.plot(data3[0],data3[1],data3[2],lw=2, color = "c")[0]
line4 = plt.plot(data4[0],data4[1],data4[2],lw=2, color = "y")[0]
line5 = plt.plot(data5[0],data5[1],data5[2],lw=2,color ='orange')[0]
line6 = plt.plot(data6[0],data6[1],data6[2],lw=2,color ='brown')[0]
ani = animation.FuncAnimation(fig, func, frames=num_data,fargs=(data1,data2,data3,data4,data5,data6, line1,line2,line3,line4,line5,line6),
                            interval=5, blit=False)
plt.legend(['earth','sun','Mercury','Venus','Mars','Jupiter'])
plt.show()
f = r"c://Users/ab/Desktop/animation.gif" 
writergif = animation.PillowWriter(fps=30) 
ani.save(f, writer=writergif)