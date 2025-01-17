import numpy as np
import matplotlib.pyplot as mp


#Defines the Decay Function
def Decay_Function(n, x, h):
    y = n * np.e ** (-h * x)
    return y

#variables
n = 100
x = np.linspace(0,100,100)
h = [0.05, 0.2, 0.5, 2.0]

#store data in dictionary
results = {}

#for loop to run through multiple lambda values
for i in h:
    Decay_Function(n, x, i)
    y = Decay_Function(n, x, i)
    results[i] = y


#plot the dictionaries
for label in results:
    mp.plot(x, results[label], label=f"λ={label}")

#create plot and show the plot and save as png
mp.xlabel("Time (s)")
mp.ylabel("Number of Radioactive Atoms")
mp.title("Radioactive Decay with Varying λ")
mp.legend(loc='upper right', title='Decay Constant')
mp.grid()
mp.savefig("Radioactive_Decay.png")
mp.show()





