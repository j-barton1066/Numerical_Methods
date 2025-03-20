import numpy as np
import matplotlib.pyplot as plt
from adjustText import adjust_text

def altitudegraph(z0, m, c, g, v0, t):
    return z0 + (m / c * (v0 + ((m * g) / c)) * (1 - np.exp(-(c/m)*t)) - (m * g / c) * t)

def max_altitude(z0, m, c, g, v0):
    #calculate the time to reach max altitude
    t_max = m / c * np.log(1 + c * v0 / (m * g))
    #calculate the max altitude
    z_max = altitudegraph(z0, m, c, g, v0, t_max)
    return z_max, t_max


#Parabolic Method
def parabolic_method(func, x0, x1, x2, tol=0.5, max_iter=100):
    for i in range(max_iter):
        f0 = func(x0)
        f1 = func(x1)
        f2 = func(x2)

        numerator = (f0*(x1**2 - x2**2))+ (f1*(x2**2 - x0**2)) + (f2*(x0**2 - x1**2))
        denominator = (f0 * (x1 - x2) + f1 * (x2 - x0) + f2 * (x0 - x1)) * 2

        if abs(denominator) < 1e-10:
            return x1
        x3 = numerator / denominator
        if abs(x3-x1) < tol:
            return x3
        
        x0 = x1
        x1 = x2
        x2 = x3
    return x1

def random_search(ke, g, num_samples=10000):
    z0 = 10 #m
    c = 8 #kg/s
    best_m = None
    best_v0 = None
    best_z_max = -np.inf
    for _ in range(num_samples):
        m = np.random.uniform(0.1, 150)
        v0 = np.sqrt(2 * ke / m)
        z_max, _ = max_altitude(z0, m, c, g, v0)
        if z_max > best_z_max:
            best_z_max = z_max
            best_m = m
            best_v0 = v0
    return best_m, best_v0, best_z_max
    
def main():
    g = 9.81 # m/s^2
    z0 = 100 # m
    v0 = 11.2 # m/s
    m = 100 # kg
    c = 5 #kg/s
    t_values =  np.linspace(0, 2.5, 1000)
    func = lambda t: altitudegraph(z0, m, c, g, v0, t)
    ke = 1500 #J
    x0 = 0
    x1 = 1
    x2 = 2
    z = []
    for t in t_values:
        z.append(altitudegraph(z0, m, c, g, v0, t))
    z_max, t_max = max_altitude(z0, m, c, g, v0)
    print("The max altitude is: ", z_max)
    print("The time to reach max altitude is: ", t_max)

    #paraoblic method
    x_max = parabolic_method(func, x0, x1, x2)
    print("The time to reach max altitude using parabolic method is: ", x_max)
    print("The max altitude using parabolic method is: ", altitudegraph(z0, m, c, g, v0, x_max))

    #random search
    print("Random Search using the inital height of 10m")
    best_m, best_v0, best_z_max = random_search(ke, g)
    print("The best mass is: ", best_m, "kg")
    print("The best initial velocity is: ", best_v0, "m/s")
    print("The max altitude is: ", best_z_max , "m")

    texts = []
    plt.plot(t_values, z)
    plt.scatter(t_max, z_max, color = "red", label = "Max Altitude")
    text1 = f"Max Altitude: {z_max:.2f} m"
    texts.append(text1)
    plt.annotate(text1, (t_max, z_max), xytext=(1.5, z_max), 
                 arrowprops=dict(arrowstyle="->", color='black'),
                 fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Altitude vs Time")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
