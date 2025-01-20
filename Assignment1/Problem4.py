#Problem 4
#J Barton
#A02298690
import numpy as np
import matplotlib.pyplot as mp
from scipy.integrate import ode

from Problem2 import label

g = 9.8 #m/s^2
m = 9.8 #kg
c = 49.5 #kg/s
v_0 = 0 #m/s
start = 0 #s
stop = 1.5 #s
num = 10
t = np.linspace(start, stop, num)
dt = 0.1

#defines terminal velocity
def terminalvelocity(g,m,c):
    v_T = (g * m) / c
    return v_T

#defines velocity as a function of time
def velocitycalc(m,c,v_T,t):
    v = v_T  * (1 - np.exp(-(c / m) * t))
    return v

# #Defines the ODE for velocity
# def odevelocity(g,m,c,stop,dt):
#     time = np.arange(start,stop,dt)
#     velocity = np.zeros(len(time))
#     for i in range(len(time)):
#         velocity[i] = velocity[i - 1] + (g - (c/m) * velocity[i - 1]) * dt
#     return velocity, time

v_T = terminalvelocity(g,m,c)
v = velocitycalc(m,c,v_T,t)
print(velocitycalc(m, c, t, v_T))
# time, velocity = odevelocity(g,m,c,stop,dt)
# print(odevelocity(g,m,c,stop,dt))

#create plot and show the plot and save as png
# mp.plot(time,velocity, label = "ODE")
mp.plot(t, v, label = "Velocity")
mp.xlabel("Time (s)")
mp.ylabel("Velocity (m/s)")
mp.title("")
mp.legend(loc='upper right')
mp.grid()
#plot.savefig("Radioactive_Decay.png")
mp.show()



