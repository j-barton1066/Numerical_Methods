#Problem 1
#J Barton
#A02298690

import numpy as np


def quadform(p, q, r):
    x_1 = (-q + np.sqrt((q ** 2) - 4 * (p * r))) / (2 * p)
    x_2 = (-q - np.sqrt((q ** 2) - 4 * (p * r))) / (2 * p)
    return x_1, x_2


def rootcheck(p, q, r):
    if q ** 2 > 4 * (p * r):
        #Two real roots
        print("There are two real roots")
        answer1 = np.float64(quadform(p,q, r)[0])
        answer2 = np.float64(quadform(p,q, r)[1])
        print(f"{answer1}, {answer2}")
    elif q ** 2 < 4 * (p * r):
        #Two complex roots
        print("There are two imaginary roots")
    elif q ** 2 == 4 * (p * r):
        #One real root
        print("There is one real root")
        answer1 = np.float64(quadform(p, q, r)[0])
        answer2 = np.float64(quadform(p, q, r)[1])
        if answer1 == answer2:
            print(f"{answer1}")

p = 1
q = -7
r = 10
rootcheck(p, q, r)


