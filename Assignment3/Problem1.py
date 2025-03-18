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
