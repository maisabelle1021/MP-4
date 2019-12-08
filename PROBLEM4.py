import math as mh
import numpy as np
import matplotlib.pyplot as plt

h = float(input("Height of projectile from the ground (in meters): "))
v = float(input("Velocity in m/s: "))
ang = mh.radians(float(input("Angle (in degrees) with respect to the x-axis: ")))
a_x = float(input("x-component of acceleration (in m/s^2): "))
a_y = float(input ("y-component of acceleration (in m/s^2): "))

if a_y == 0.0:
    print("ERROR: If vertical acceleration is 0 m/s^2, there is no free fall.")
    
#velocity x-component
v_iny = v*mh.sin(ang)
v_inx = v*mh.cos(ang)
t_in = 0
t_fin = (mh.sqrt(pow(v_iny,2)-(2*a_y*h))-v_iny)/a_y



if t_fin <=0.0:
    t_fin = -(mh.sqrt(mh.pow(v*mh.sin(ang),2)-(2*a_y*h)-(v*mh.sin(ang))))/a_y

t = np.arange(0,t_fin+1,t_fin/100)

y = v_iny*t + (a_y*(pow(t,2)))/2+h
x = v_inx*t + (a_x*(pow(t,2)))/2

fig = plt.figure(figsize=(9,6))
fig2 = plt.plot(x,y, label="y(m)")
plt.xlabel('Horizontal Range')
plt.ylabel('Height')
plt.title('Projectile Motion Trajectory')
plt.show()
