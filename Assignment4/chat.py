import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def Reynolds_number(vel, diam, nu):
    """Compute the particle Reynolds number."""
    return vel * diam / nu


def drag_coefficient(Re):
    """Estimate drag coefficient from Reynolds number."""
    return 24/Re + 1.5


def droplet_deriv(t, state, mass, area, diam, rho_air, mu_air, rho_droplet, g):
    """
    ODE system for droplet motion:
      state = [x, y, u, v]
    where x, y = positions; u, v = velocities (horizontal, vertical).
    """
    x, y, u, v = state
    vel = np.hypot(u, v)
    Re = Reynolds_number(vel, diam, mu_air)
    Cd = drag_coefficient(Re)
    drag = 0.5 * Cd * rho_air * area * vel**2
    if vel > 0:
        drag_u = drag * (u/vel)
        drag_v = drag * (v/vel)
    else:
        drag_u = drag_v = 0.0
    du_dt = -drag_u / mass
    dv_dt = -drag_v / mass + (1 - rho_air/rho_droplet)*g
    return [u, -v, du_dt, dv_dt]


def ground_event(t, state, h):
    """Event: droplet reaches the floor (y=0)."""
    return state[1]
ground_event.terminal = True
ground_event.direction = -1


def main():
    # Physical parameters
    rho_droplet = 1000.0  # kg/m^3
    rho_air = 1.2         # kg/m^3
    mu_air = 1.48e-5      # m^2/s (kinematic viscosity)
    g = 9.81              # m/s^2 (gravity)
    height = 1.75         # m, release height

    # Droplet sizes (m)
    diameters = np.array([1,2,4,8,16,32,64,128]) * 1e-6
    radii = diameters / 2
    volumes = 4/3 * np.pi * radii**3
    areas = np.pi * radii**2
    masses = volumes * rho_droplet

    # Initial respiratory speeds (m/s)
    speeds = [1.5, 10, 20, 30, 40, 50]

    # Time span and step
    t_span = (0, 10*60)   # seconds
    max_step = 10       # s

    # Containers for results
    trajectories = {}
    fall_times = {}

    # Run integrations
    for speed in speeds:
        for diam, mass, area in zip(diameters, masses, areas):
            sol = solve_ivp(
                fun=lambda t, y, mass=mass, area=area, diam=diam: droplet_deriv(
                    t, y, mass, area, diam,
                    rho_air, mu_air, rho_droplet, g
                ),
                t_span=t_span,
                y0=[0, height, speed, 0],
                events=lambda t, y, h=height: ground_event(t, y, h),
                max_step=max_step,
                rtol=1e-3, atol=1e-6
            )
            trajectories[(speed, diam)] = sol
            # record fall time
            if sol.t_events[0].size > 0:
                fall_times[(speed, diam)] = sol.t_events[0][0]
            else:
                fall_times[(speed, diam)] = sol.t[-1]

    # Print fall times (in minutes)
    print("Fall times (min):")
    for speed in speeds:
        row = [fall_times[(speed, d)]/60 for d in diameters]
        print(f"{speed} m/s: {[f'{t:.2f}' for t in row]}")

    # Plot height vs time
    plt.figure(figsize=(8,5))
    for (speed, diam), sol in trajectories.items():
        t_min = sol.t / 60.0
        y_pos = sol.y[1]
        plt.plot(
            t_min, y_pos,
            label=f"{diam*1e6:.0f} μm @ {speed:.0f} m/s"
        )

    plt.xlabel('Time (min)')
    plt.ylabel('Height above floor (m)')
    plt.title('Droplet Height vs Time for Various Sizes & Speeds')
    plt.ylim(0, height*1.05)
    plt.legend(fontsize='small', ncol=2)
    plt.grid(ls='--', alpha=0.4)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
