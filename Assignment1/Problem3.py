#Problem 3
#J Barton
#A02298690

import numpy as np
from scipy import stats
#generate array
numlist = np.random.randint(0,101, size=20)

#create list and convert array to list
list = []

for i in numlist:
    list.append(int(i))
print(list)

#Put list in reverse order
list.sort(reverse=True)
print(list)

mean = np.mean(list)
median = np.median(list)
mode = stats.mode(list)

print("Mean: ", mean)
print("Meadian: ", median)
print("Mode: ", mode)