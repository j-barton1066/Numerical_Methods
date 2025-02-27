import numpy as np
import matplotlib.pyplot as plt

#equation = (1/np.sqrt(f)) + 2.0 * np.log10((e/(3.7* d))+(2.51/(Re* np.sqrt(f))))

#solve for f
def colebrook(f, Re, p, d):
    return (1/np.sqrt(f)) + 2.0 * np.log10((p/(3.7* d))+(2.51/(Re* np.sqrt(f))))

def SwameeJain(Re, d, p):
    return 1.325 / (np.log(p/(3.7*d) + 5.74/(Re ** 0.9))) ** 2

def ModifiedSecant(f0, f1, p, d, Re):
    tol = .0001
    max_iter = 10000
    for i in range(max_iter):
        F_f0 = colebrook(f0, Re, p, d)
        F_f1 = colebrook(f1, Re, p, d)
        f = f1 - F_f1 * (f1 - f0) / (F_f1 - F_f0)
        if abs(f - f1) < tol:
            return f
        f0 = f1
        f1 = f
    return np.nan



def main():
    p = 0.01/1000 # mm to m
    Re_values = np.arange(1e4, 1e6, 10000)
    d_values = np.arange(2, 20, 0.5)
    f0 = 0.08
    f1 = 0.008

    f_values = np.full((len(d_values), len(Re_values)), np.nan)
    for i, d in enumerate(d_values):
        for j, Re in enumerate(Re_values):
            if  np.isnan(f_values[i, j]):
                f_values[i, j] = ModifiedSecant(f0, f1, p, d, Re)
    
    for i, d in enumerate(d_values):
        for j, Re in enumerate(Re_values):
            if  np.isnan(f_values[i, j]):
                f_values[i, j] = SwameeJain(Re, d, p)

    Re_range, D_range = np.meshgrid(Re_values, d_values)
    
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
                                           