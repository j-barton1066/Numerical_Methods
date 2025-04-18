import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def Reynolds_number(velocity, diameter, viscosity):
    return (velocity * diameter) / viscosity

def drag_coefficient(Re):
    return (24/Re) + 1.5


def main():
    #Ambient Parameters
    rho_droplet = 1000 # kg/m^3
    rho_air = 1.2 # kg/m^3
    mu_air = 1.48e-5 # m^2/s
    g = 9.81 # m/s^2

    #Droplet Parameters
    droplet_diameter = np.array([1e-6, 2e-6, 4e-6, 8e-6, 1.6e-5, 3.2e-5, 6.4e-5, 1.28e-4]) # m
    radius = np.array([]) # m
    V_droplet = np.array([]) # m^3
    A_droplet = np.array([]) # m^2
    mass_droplet = np.array([]) # kg
    for i in range(len(droplet_diameter)):
        radius = np.append(radius, droplet_diameter[i]/2)
        V_droplet = np.append(V_droplet, (4/3)*np.pi*(radius[i]**3))
        A_droplet = np.append(A_droplet, np.pi*(radius[i]**2))
        mass_droplet = np.append(mass_droplet, (np.pi/6)*(droplet_diameter[i]**3)*rho_droplet)
    
    #Initial Conditons
    h = 1.75 # m (initial height)
    u0 = np.array([1.5, 10, 20, 30, 40, 50]) # m/s (initial velocity)
    initial_conditions = np.array([0, h, u0, 0]) # m, m/s [x0, y0, u0,v0]
    # Time Parameters
    t_span = (0, 10) # s
    delta_t = 0.01 # s

    solver = sp.integrate.solve_ivp(
        fun = lambda t, state: droplet_deriv(t, state, m, A, D, rho_air, mu_air, g),
        t_span = t_span,
        y0 = initial_conditions,
        method = 'RK45',
        events = lambda t, state: ground_event(t, state, h),
        rtol = 1e-6,
        atol = 1e-9,
    )

    t_values = solver.t
    x_values = solver.y[0]
    y_values = solver.y[1]

    
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
    