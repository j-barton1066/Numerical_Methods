#Problem 3
#J Barton
#A02298690

import numpy as np
from scipy import stats
#generate array
rannum = np.random.randint(0,101, size=20)

#create list and convert array to list
numlist = []

for i in rannum:
    numlist.append(int(i))
#print(list)

#Put list in reverse order
numlist.sort(reverse=True)
print(numlist)

mean = np.mean(numlist)
median = np.median(numlist)
mode = stats.mode(numlist)
modelist = []
modevalue = numlist.append(int(mode.mode))

print("Mean: ", mean)
print("Median: ", median)
if len(modelist) == 0:
    print("Mode: All numbers are represented once")
else:
    print(f"Mode: {',' .join(map(str, modelist))}")