import numpy as np
import matplotlib.pyplot as plt

#equation = (1/np.sqrt(f)) + 2.0 * np.log10((e/(3.7* d))+(2.51/(Re* np.sqrt(f))))

#solve for f
def colebrook(f, Re, e, d):
    return (1/np.sqrt(f)) + 2.0 * np.log10((e/(3.7* d))+(2.51/(Re* np.sqrt(f))))

def SwameeJain(Re, d, e):
    return 1.325 / (np.log(e/(3.7*d) + 5.74/(Re ** 0.9))) ** 2

def ModifiedSecant(f0, f1, e, d, Re):
    tol = .0001
    max_iter = 10000
    for i in range(max_iter):
        F_f0 = colebrook(f0, Re, e, d)
        F_f1 = colebrook(f1, Re, e, d)
        f = f1 - F_f1 * (f1 - f0) / (F_f1 - F_f0)
        if abs(f - f1) < tol:
            return f
        f0 = f1
        f1 = f
    return np.nan

def volume_flow(V,D):
    return V * np.pi * D ** 2 / 4

def velocity(Re,D,p,u):
    return Re * u / (p * D)

def pressure_gradient(f, D, p, Q):
    return f * ((2 * p) / (np.pi ** 2 * D ** 3)) * Q ** 2
    

def main():
    e = 0.01/1000 # mm to m
    Re_values = np.arange(1e4, 1e6, 10000)
    d_values = np.arange(2, 20, 0.5)
    f0 = 0.08
    f1 = 0.008
    D = 5
    p = 1000 # kg/m^3
    g = 9.81 # m/s^2
    u = 10e-3 # Pa.s
    
    

    f_values = np.full((len(d_values), len(Re_values)), np.nan)
    for i, d in enumerate(d_values):
        for j, Re in enumerate(Re_values):
            if  np.isnan(f_values[i, j]):
                f_values[i, j] = ModifiedSecant(f0, f1, e, d, Re)
    
    for i, d in enumerate(d_values):
        for j, Re in enumerate(Re_values):
            if  np.isnan(f_values[i, j]):
                f_values[i, j] = SwameeJain(Re, d, e)



    #Pressure Gradient
    fr = []
    V = []
    for i, Re in enumerate(Re_values):
        fr.append(SwameeJain(Re, D, e))
        V.append(velocity(Re, D, p, u))
    Q = []
    for i, v in enumerate(V):
        Q.append(volume_flow(v, D))
    pg = []
    for i in range(len(Q)):
        pg.append(pressure_gradient(fr[i], D, p, Q[i]))
        
    plt.xlabel('Volume Flow Rate (m^3/s)')
    plt.ylabel('Pressure Gradient (Pa/m)')
    plt.title('Pressure Gradient vs. Volume Flow Rate')
    plt.plot(Q, pg)


    Re_range, D_range = np.meshgrid(Re_values, d_values)
    #print(f_values)
    
    #plot the friction factor as reference from assignment 2
    fig, ax = plt.subplots(1, 2, figsize=(14,6))
    contour1 = ax[0].contourf(Re_range, D_range, f_values, levels=100, cmap='viridis')
    # Plot friction factor vs. Reynolds number and pipe diameter
    
    
    ax[0].set_xlabel('Reynolds Number (Re)')
    ax[0].set_ylabel('Pipe Diameter (m)')
    ax[0].set_title("Colebrook Equation\n Friction Factor vs. Reynolds Number and Pipe Diameter")

    #Swamee Jain Friction Factor
    contour2 = ax[1].contourf(Re_range, D_range, f_values, levels=100, cmap='viridis')
    fig.colorbar(contour2, ax=ax[1], label='Friction Factor')
    ax[1].set_xlabel('Reynolds Number (Re)')
    ax[1].set_ylabel('Pipe Diameter (m)')
    ax[1].set_title('Swamee Jain \n Friction Factor vs. Reynolds Number and Pipe Diameter')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
                                           