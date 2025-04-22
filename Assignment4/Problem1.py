import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def Reynolds_number(velocity, diameter, viscosity):
    return (velocity * diameter) / viscosity

def drag_coefficient(Re):
    return (24/Re) + 1.5

<<<<<<< HEAD
<<<<<<< HEAD
def droplet_deriv(t, state, m, A, D, rho_air, mu_air, rho_droplet, g):
    x, y, u, v = state
    vel = np.sqrt(u**2 + v**2)
    Re = Reynolds_number(vel, D, mu_air)
    Cd = drag_coefficient(Re)
    F_drag = 0.5 * rho_air * A * Cd * vel**2
    
    if vel > 0:
        drag_u = F_drag * (u / vel)
        drag_v = F_drag * (v / vel)
    else:
        drag_u = drag_v = 0
        
    drag_u = -drag_u / m
    drag_v = -drag_v / m - (1 - rho_air/rho_droplet) * g
    return [u, v, drag_u, drag_v]

def ground_event(t, state, h):
    return state[1]
ground_event.terminal = True
ground_event.direction = -1

=======
>>>>>>> parent of 5746c6f (working on problem1)
=======
>>>>>>> parent of 5746c6f (working on problem1)

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

    
<<<<<<< HEAD
<<<<<<< HEAD
    t_span = (0, 20*60) # s
    max_dt = 1
    first_times    = {}
    last_times     = {}
    first_states   = {}
    last_states    = {}

    for speed in u0:
        distances     = []
        fall_times    = []
        first_times[speed]  = []
        last_times[speed]   = []
        first_states[speed] = []
        last_states[speed]  = []

        for D, mi, Ai in zip(droplet_diameter, mass_droplet, A_droplet):
            sol = solve_ivp(
                fun=lambda t, st: droplet_deriv(t, st, mi, Ai, D, rho_air, mu_air, rho_droplet, g),
                t_span=t_span,
                y0=[0, h, speed, 0],
                method='RK45',
                events=lambda t, st: ground_event(t, st, h),
                max_step=max_dt,
                rtol=1e-6, atol=1e-9
            )

            # record first & last times
            first_times[speed].append(sol.t[0])
            last_times[speed].append(sol.t[-1])

            # record first & last states (x, y, u, v)
            first_states[speed].append(sol.y[:, 0].copy())
            last_states[speed].append(sol.y[:, -1].copy())

            # your existing outputs
            distances.append(sol.y[0, -1])
            fall_times.append(sol.t[0] if sol.t_events[0].size==0 else sol.t_events[0][0])

        results[speed] = distances
        times[speed]   = fall_times

    # at the end you can print them however you like, e.g.:
    for speed in u0:
        for i, D in enumerate(droplet_diameter):
            print(f"{speed} m/s, D={D*1e6:.1f} µm → "
                  f"t_start={first_times[speed][i]:.2f}s, "
                  f"state_start={first_states[speed][i]}, "
                  f"t_end={last_times[speed][i]:.2f}s, "
                  f"state_end={last_states[speed][i]}")
    # times = {}
    # results = {}
    # for speed in u0:
    #     distances = []
    #     fall_times = []
    #     for D, mi, Ai in zip(droplet_diameter, mass_droplet, A_droplet):
    #         sol = solve_ivp(
    #             fun=lambda t, st: droplet_deriv(t, st, mi, Ai, D, rho_air, mu_air, rho_droplet, g),
    #             t_span=t_span,
    #             y0=[0, h, speed, 0],
    #             method='RK45',
    #             events=lambda t, st: ground_event(t, st, h),
    #             max_step=max_dt,
    #             rtol=1e-6, atol=1e-9
    #         )
    #         distances.append(sol.y[0, -1])
    #         if sol.t_events[0].size > 0:
    #             fall_times.append(sol.t_events[0][0])
    #         else:
    #             fall_times.append(sol.t[-1])
    #     results[speed] = distances
    #     times[speed] = fall_times
        

    # for speed, t_list in times.items():
    #     print(f"{speed} m/s fall times (s):",
    #           [f"{t:.2f}" for t in t_list])

    plt.figure(figsize=(8,5))

    # Outer loop over each expiratory speed
    for speed in u0:
        # Inner loop over each droplet diameter
        for D, m, A in zip(droplet_diameter, mass_droplet, A_droplet):
            sol = solve_ivp(
                fun=lambda t, y: droplet_deriv(t, y, m, A, D,
                                            rho_air, mu_air, rho_droplet, g),
                t_span=t_span,
                y0=[0, h, speed, 0],                     # use scalar speed
                events=lambda t, y: ground_event(t, y, h),
                max_step=max_dt,
                rtol=1e-6, atol=1e-9
            )
            # convert to minutes with true float division
            
            y_pos = sol.y[1]

            plt.plot(
                sol.t, y_pos,
                label=f'{D*1e6:.1f} µm @ {speed:.0f} m/s'
            )

    plt.xlabel('Time (seconds)')
    plt.ylabel('Height above floor (m)')
    plt.title('Droplet Height vs Time for Various Sizes & Speeds')
    plt.ylim(0, h*1.05)
    plt.legend(loc='best', fontsize='small', ncol=2)
    plt.grid(ls='--', alpha=0.4)
    plt.tight_layout()
    plt.show()
=======
    # print("Reynolds Number:")
    # print(Re)   
    # print("Velocity(m/s):", v_droplet)
    # print("Droplet Diameter (m):", droplet_diameter)
    # print("Droplet Radius (m):", radius)
    # print("Droplet Volume (m^3):", V_droplet)
    # print("Droplet Surface Area (m^2):", A_droplet)
    # print("Droplet Mass (kg):", mass_droplet)

>>>>>>> parent of 5746c6f (working on problem1)
=======
    # print("Reynolds Number:")
    # print(Re)   
    # print("Velocity(m/s):", v_droplet)
    # print("Droplet Diameter (m):", droplet_diameter)
    # print("Droplet Radius (m):", radius)
    # print("Droplet Volume (m^3):", V_droplet)
    # print("Droplet Surface Area (m^2):", A_droplet)
    # print("Droplet Mass (kg):", mass_droplet)

>>>>>>> parent of 5746c6f (working on problem1)

if __name__ == "__main__":
    main()
    