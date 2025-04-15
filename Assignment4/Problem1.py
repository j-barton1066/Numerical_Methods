import matplotlib.pyplot as plt
import numpy as np

def Reynolds_number(velocity, diameter, viscosity):
    return (velocity * diameter) / viscosity

def drag_coefficient(Re):
    return (24/Re) + 1.5


def main():
    droplet_diameter = np.array([1e-6, 2e-6, 4e-6, 8e-6, 1.6e-5, 3.2e-5, 6.4e-5, 1.28e-4]) # m
    v_droplet = np.linspace(1.5,50,5) # m/s
    #Ambient Parameters
    rho_droplet = 1000 # kg/m^3
    rho_air = 1.2 # kg/m^3
    mu_air = 1.8e-5 # kg/(m*s) or Pa*s
    g = 9.81 # m/s^2
    h = 1.75 # m
    max_time = 10 # s
    delta_t = 1e-4 # s

    #Droplet Parameters
    radius = np.array([]) # m
    V_droplet = np.array([]) # m^3
    A_droplet = np.array([]) # m^2
    mass_droplet = np.array([]) # kg
    for i in range(len(droplet_diameter)):
        radius = np.append(radius, droplet_diameter[i]/2)
        V_droplet = np.append(V_droplet, (4/3)*np.pi*(radius[i]**3))
        A_droplet = np.append(A_droplet, np.pi*(radius[i]**2))
        mass_droplet = np.append(mass_droplet, (np.pi/6)*(droplet_diameter[i]**3)*rho_droplet)

    # Calculate Reynolds number for each droplet diameter and velocity
    Re = np.zeros((len(droplet_diameter), len(v_droplet)))
    for i in range(len(droplet_diameter)):
        for j in range(len(v_droplet)):
            Re[i][j] = Reynolds_number(v_droplet[j], droplet_diameter[i], mu_air)
    
    # print("Reynolds Number:")
    # print(Re)   
    # print("Velocity(m/s):", v_droplet)
    # print("Droplet Diameter (m):", droplet_diameter)
    # print("Droplet Radius (m):", radius)
    # print("Droplet Volume (m^3):", V_droplet)
    # print("Droplet Surface Area (m^2):", A_droplet)
    # print("Droplet Mass (kg):", mass_droplet)


if __name__ == "__main__":
    main()
    