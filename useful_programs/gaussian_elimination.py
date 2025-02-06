import numpy as np
def gaussian_elimination(A,b):
    n = len(b)
    #forward elimnation
    for i in range(n):
        #Partial Pivot step
        max_row = i + np.argmax(np.abs(A[i:n,i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]] #switches rows A
            b[[i, max_row]] = b[[max_row, i]] #switches rows b
        for k in range(i+1, n):
            factor = A[k, i] / A[i, i]
            for j in range(i, n):
                A[k, j] -= factor * A[i, j]
                b[k] -= factor * b[i]
    #backward
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        #adds out of bounds condition
        x[i] = (b[i] - np.dot(A[i, i+1:] if i+1 < n else 0, x[i+1:] if i+1 < n else 0)) / A[i, i]
    return x

# A = np.array([[2,3,1], [4,1,2], [-2,5,2]], dtype=np.float64)
# b = np.array([9,3,7], dtype=np.float64)

A = np.array([[2,100000],[1,1]], dtype=np.float64)
b = np.array([100000,2], dtype=np.float64)
print(A)
print(b)
solution = gaussian_elimination(A,b)
print(solution)