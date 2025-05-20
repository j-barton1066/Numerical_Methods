import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import pandas as pd

def Reynolds_number(velocity, diameter, viscosity):
    return (velocity * diameter) / viscosity

def drag_coefficient(Re):
    return (24/Re) + 1.5

def droplet_deriv(t, state, m, A, D, rho_air, mu_air, rho_droplet, g):
    x, y, u, v = state
    vel = np.sqrt(u**2 + v**2)
    Re = Reynolds_number(vel, D, mu_air)
    Cd = drag_coefficient(Re)
    F_drag = 0.5 * rho_air * A * Cd * u**2
    
    if vel > 0:
        drag_u = F_drag * (u / vel)
        drag_v = F_drag * (v / vel)
    else:
        drag_u = 0
        drag_v = 0
    drag_u = -drag_u / m
    drag_v = -drag_v / m - (1 - rho_air/rho_droplet) * g
    return [u, v, drag_u, drag_v]

def ground_event(t, state, h):
    return state[1]
ground_event.terminal = True
ground_event.direction = -1



def main():
    #Initial Conditons
    rho_droplet = 1000 # kg/m^3
    rho_air = 1.2 # kg/m^3
    mu_air = 1.48e-5 # m^2/s
    g = 9.81 # m/s^2
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
    h = 1.75 # m (initial height)
    u0 = np.array([1.5, 10, 20, 30, 40, 50]) # m/s (initial velocity)
    # Time Parameters
    t_span = (0, 1) # s
    max_dt = 1 # s
    times = {}
    results = {}
    for speed in u0:
        distances = []
        fall_times = []
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
            distances.append(sol.y[0, -1])
            if sol.t_events[0].size > 0:
                fall_times.append(sol.t_events[0][0])
            else:
                fall_times.append(sol.t[-1])
        results[speed] = distances
        times[speed] = fall_times

    # Convert results to DataFrame for better readability
    df = pd.DataFrame(
        {f"{speed:.1f} m/s": t_list
        for speed, t_list in times.items()},
        index=[f"{D*1e6:.1f} µm" for D in droplet_diameter]
    )
    print(df.to_string())

    index = [f"{D*1e6:.1f} µm" for D in droplet_diameter]


    df_dist = pd.DataFrame(
    { f"{s:.1f} m/s": dist_list
      for s, dist_list in results.items() },
    index=index
)

    print("Horizontal distance traveled (m) by droplet size and initial speed:\n")
    print(df_dist.to_string())

    # for speed, t_list in times.items():
    #     print(f"{speed} m/s fall times (s):",
    #           [f"{t:.2f}" for t in t_list])

    plt.figure(figsize=(8,5))

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
            t_min = sol.t 
            y_pos = sol.y[1]

            plt.plot(
                t_min, y_pos,
                label=f'{D*1e6:.1f} µm @ {speed:.0f} m/s'
            )

    plt.xlabel('Time (seconds)')
    plt.ylabel('Height above floor (m)')
    plt.title('Droplet Height vs Time for Various Sizes & Speeds')
    plt.ylim(0, h*1.05)
    plt.legend(loc='best', fontsize='small', ncol=2)
    plt.grid(ls='--', alpha=0.4)
    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__":
    main()