import numpy as np
import matplotlib.pyplot as plt

def altitudegraph(z0, m, c, g, v0, t):
    return z0 + (m / c * (v0 + ((m * g) / c)) * (1 - np.exp(-(c/m)*t)) - (m * g / c) * t)

def max_altitude(z0, m, c, g, v0):
    #calculate the time to reach max altitude
    t_max = m / c * np.log(1 + c * v0 / (m * g))

    #calculate the max altitude
    z_max = altitudegraph(z0, m, c, g, v0, t_max)
    return z_max, t_max

def dzfunction(x0, v0, m, c, g):
    return v0 * np.exp(- (c/m) * x0) - (m * g / c) * (1 - np.exp(- (c/m) * x0))

def ddzfunction(x0, v0, m, c):
    return  -(c/m) * v0 * np.exp(- (c/m) * x0)

def newton_method(v0, g,c, m, x0, tol, max_iter):
    for i in range(max_iter):
        dz = dzfunction(x0, v0, m, c, g)
        ddz = ddzfunction(x0, v0, m, c)
        
        if abs(ddz) < 1e-10:
            raise ValueError("The derivative is zero")
        x1 = x0 - dz / ddz
        print(f"Iteration {i+1}: x0 = {x0:.6f}, dz = {dz:.6f}, ddz = {ddz:.6f}, x1 = {x1:.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1


def main():
    g = 9.81 # m/s^2
    z0 = 100 # m
    v0 = 11.2 # m/s
    m = 100 # kg
    c = 5 #kg/s

    t_values =  np.linspace(0, 2.5, 1000)
    z = []
    for t in t_values:
        z.append(altitudegraph(z0, m, c, g, v0, t))
    z_max, t_max = max_altitude(z0, m, c, g, v0)
    print("The max altitude is: ", z_max)
    print("The time to reach max altitude is: ", t_max)

    #newton_raphson
    x0 = 1.5
    tol = 0.5
    max_iter = 100
    x1 = newton_method(v0, g, c, m, x0, tol, max_iter)
    print("The time to reach max altitude using newton method is: ", x1)
    
    #print(z)
    plt.plot(t_values, z)
    plt.scatter(t_max, z_max, color = "red", label = "Max Altitude")
    text = f"Max Altitude: {z_max:.2f} m"
    plt.annotate(text, (t_max, z_max), xytext=(1.5, z_max), 
                 arrowprops=dict(arrowstyle="->", color='black'),
                 fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Altitude vs Time")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
