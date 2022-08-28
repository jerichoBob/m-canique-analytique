import matplotlib.pyplot as plt
import numpy as np

# Newton's equations of motion
# v(t) = v(t-1) + a(t)*t
# x(t) = x(t-1) + v(t)*t + .5*a(t)*t^2

# Newton's law of gravitation
# r_squared = (x2-x1)**2 + (y2-y1)**2
# F=G*m1*m2/r_squared

# a1 = G*m1/r_squared

# center of mass = m1*x1(t)+m2*x2(t) / (m1+m2)
# com_x = m1*x1+m2*x2 / (m1+m2)
# com_y = m1*y1+m2*y2 / (m1+m2)

# handle the boundary conditions that arise when computing tan^-1
# results will be between -np.pi/2 & np.pi/2
def my_atan(delta_y, delta_x):
    # limit = 0.000000000001;
    # if (delta_x<limit): return np.pi/2;
    return np.arctan2(delta_y,delta_x);


m1 = 5.9722 * 10**24 # earth mass
m2 = 7.342 * 10**22 # moon mass
r_moon = 400000000 # m
v_moon = 1022 # m/s
G=6.67*10**(-11)
Gmm = G*m1*m2; # precalc cuz they ain't changin'
# v for any orbital mass 
# a = g = v^2/r = G * m1 /r^2
# v^2 = G * m1 /r
# v = sqrt (G * m1 / r) -- escape velocity

# protection when r_squared goes to shit (== 0)
def my_F(x1, x2, y1, y2, debug):
    limit = 0.0000001; # only get so close to each other
    r_squared = (x2-x1)**2 + (y2-y1)**2;
    if (r_squared > limit): F= Gmm /r_squared;
    else: F=Gmm / limit;
    if (debug): print("F=",F);
    if (debug): print("==== r_squared: ",r_squared);    
    if (debug): print("r_sqrt: ", np.sqrt(r_squared));
    return F;

# initial conditions
t=0;
delta_t = 5;
DEBUG = 0;

# mass #1 - be the earth at the origin
px1_i = 0; py1_i = 0;
vx1_i = 0; vy1_i = 0;
px1 = px1_i; py1 = py1_i; 
vx1 = vx1_i; vy1 = vy1_i; 

# mass #2 - be the moon
px2_i = 0; py2_i = r_moon;
vx2_i = v_moon; vy2_i = 0; # only x velocity, no y velocity
px2 = px2_i; py2 = py2_i; 
vx2 = vx2_i; vy2 = vy2_i; 

# containers (for plot data)
x1=[];
y1=[];
x2=[];
y2=[];

# main loop
for i in range(0,delta_t*1000):
    if (DEBUG): print("--------",i,"---------------");
    # calc F based on current coordinates of m1 & m2    
    F = my_F(px1, px2, py1, py2, DEBUG);
        
    # calc angle based on coordinates (pi correction may be needed)
    rad = my_atan((py2-py1),(px2-px1));
    
    deg = np.rad2deg(rad);
    if (DEBUG): print("deg: ",deg);    
    # if (DEBUG): print("m1: ",m1);    
    # if (DEBUG): print("m2: ",m2);    
    
    # calc acc mag, acc_x, acc_y for m1 & m2
    a1 = F / m1;
    if (DEBUG): print("a1: ",a1);    

    ax1 = a1 * np.cos(rad);
    ay1 = a1 * np.sin(rad);
    
    a2 = F / m2;
    if (DEBUG): print("a2: ",a2);        
    ax2 = a2 * np.cos(rad + np.pi);
    ay2 = a2 * np.sin(rad + np.pi);
    if (DEBUG): print("@t=",t,"(ax1,ay1,ax2,ay2)=",round(ax1,5),round(ay1,5),round(ax2,5),round(ay2,5) )

    # save values - iteration completed
    
    if (DEBUG): print("@t=",t,"(x1,y1,x2,y2)=",round(px1,5),round(py1,5),round(px2,5),round(py2,5) )
    x1.append(px1);
    y1.append(py1);
    x2.append(px2);
    y2.append(py2);
    
    # plt.quiver(xpos1, ypos1, xacc1, yacc1, scale=0.005);
    # plt.quiver(px2, py2, ax2, ay2, scale=0.002);
    

    # velocity and position should be updated
    # calc vel mag, vel_x, vel_y for m1 & m2 (update priors :) 
    # v(t) = v(t-1) + a(t)*t
    
    vx1 += ax1 * t;
    vy1 += ay1 * t;    
    vx2 += ax2 * t;
    vy2 += ay2 * t;    
    
    if (DEBUG): print("@t=",t,"(vx1,vy1,vx2,vy2)=",round(vx1,5),round(vy1,5),round(vx2,5),round(vy2,5) )

    # calc pos mag, pos_x, pos_y for m1 & m2
    # x(t) = x(t-1) + v(t)*t + .5*a(t)*t^2

    px1 += vx1 * t;
    py1 += vy1 * t;
    px2 += vx2 * t;
    py2 += vy2 * t;
    
    # get a new time before starting a new round
    t += delta_t;
    

size = 6
fig = plt.figure(figsize=(3 * size, 1.3*size), constrained_layout=True)
axs = fig.subplot_mosaic([["width", "alpha"]])

plt.scatter(x1, y1, s=100, marker ="o")
plt.scatter(x2, y2, marker ="+", linewidths = 1)
plt.show()


