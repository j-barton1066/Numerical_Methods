import numpy as np
import matplotlib.pyplot as plt

def altitudegraph(z0, m, c, g, v0, t):
    return z0 + (m / c) * (v0 + ((m * g) / c)) * (1 - np.exp(-(c/m)*t)) - (m * g / c) * t

def max_altitude(z0, m, c, g, v0):
    # Calculate time to reach max altitude (when velocity = 0)
    t_max = (m / c) * np.log(1 + (c * v0) / (m * g))

    # Calculate the max altitude
    z_max = altitudegraph(z0, m, c, g, v0, t_max)
    return z_max, t_max

def dzfunction(t, v0, m, c, g):
    return v0 * np.exp(- (c/m) * t) - (m * g / c) * (1 - np.exp(- (c/m) * t))

def ddzfunction(t, v0, m, c):
    return -(c/m) * v0 * np.exp(- (c/m) * t)

def newton_method(v0, g, c, m, x0, tol, max_iter):
    for i in range(max_iter):
        dz = dzfunction(x0, v0, m, c, g)
        ddz = ddzfunction(x0, v0, m, c)

        if abs(ddz) < 1e-10:  # Small denominator check
            print("Warning: Derivative is too small, stopping iteration.")
            return x0  # Return current estimate
        
        x1 = x0 - dz / ddz
        print(f"Iteration {i+1}: x0 = {x0:.6f}, dz = {dz:.6f}, ddz = {ddz:.6f}, x1 = {x1:.6f}")

        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

    print("Warning: Newton method did not converge within max iterations.")
    return x0  # Return the best estimate

def main():
    g = 9.81  # m/s²
    z0 = 100  # m
    v0 = 11.2  # m/s
    m = 100  # kg
    c = 5  # kg/s

    # Time values for plotting
    t_values = np.linspace(0, 2.5, 1000)
    z = [altitudegraph(z0, m, c, g, v0, t) for t in t_values]  # Optimized list comprehension

    # Compute max altitude
    z_max, t_max = max_altitude(z0, m, c, g, v0)
    print("Max altitude:", z_max)
    print("Time to max altitude:", t_max)

    # Newton-Raphson Method
    x0 = t_max
    tol = 0.5
    max_iter = 100
    x1 = newton_method(v0, g, c, m, x0, tol, max_iter)
    print("Time to max altitude using Newton method:", x1)

    # Plot altitude vs. time
    plt.plot(t_values, z, label="Altitude")
    plt.scatter(t_max, z_max, color="red", label="Max Altitude")
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
