#Problem 4
#J Barton
#A02298690
import numpy as np
import matplotlib.pyplot as mp


g = 9.8 #m/s^2
#First half of problems mass
#m = 9.8 #kg
#Problem d mass
m = 98 #kg
c = 49.5 #kg/s
v_0 = 0 #m/s
start = 0 #s
stop = 1.5 #s
num = 100
t = np.linspace(start, stop, num)
#Problem B
#dt = 0.1
#Problem C max delta d
dt = 0.01


#defines terminal velocity
def terminalvelocity(g,m,c):
    v_T = (g * m) / c
    return v_T

#defines velocity as a function of time
def velocitycalc(m,c,v_T,t):
    v = v_T  * (1 - np.exp(-(c / m) * t))
    return v

#Defines the ODE for velocity
def odevelocity(g,m,c,stop,dt):
    time = np.arange(start,stop,dt)
    y = np.zeros_like(time)
    v_0 = 0 #m/s
    y[0] = v_0
    for t in range(1,len(time)):
        y[t] = y[t-1] + (g - (c/m) * y[t-1]) * dt
    return time,y

#Find 99.99% of the Terminal Velocity
def v_target(v_T):
    t = np.linspace(0,100,1000)
    v = velocitycalc(m,c,v_T,t)
    #print(v)
    v_99 = 0.9999 * v_T
    #print(v_target)
    time_to_terminal = t[np.where(v >= v_99)[0][0]]
    #print(time_to_terminal)
    return time_to_terminal, v_99


v_T = terminalvelocity(g,m,c)
v = velocitycalc(m,c,v_T,t)
v_target(v_T)
#debug
#print(velocitycalc(m, c, t, v_T))
time, y = odevelocity(g,m,c,stop,dt)
#debug
#print(odevelocity(g,m,c,stop,dt))


time_to_terminal, v_99 = v_target(v_T)
print(f"99.99% of the terminal velocity is: {v_99: .4f} meters/second")
print(f"It will take: {time_to_terminal: .4f} seconds")


#create plot and show the plot and save as png
mp.plot(time,y, label = "ODE")
mp.plot(t, v, label = "Velocity")
mp.xlabel("Time (s)")
mp.ylabel("Velocity (m/s)")
mp.title("")
mp.legend(loc='upper right')
mp.grid()
#mp.savefig("Problem4_PartC.png")
mp.show()



