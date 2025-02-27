#Gauss Elimination with Partial Pivoting for an N x N matrix
import numpy as np
def create_matrix(n):
    matrix = []
    print(f"Enter the {n} x {n} matrix by rows: ")
    for i in range(n):
        while True:
            row_list = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row_list) == n:
                break
            else:
                print("Please enter a valid matrix.")
        matrix.append(row_list)
    matrix = np.array(matrix, dtype=float)
    return matrix

def solution_matrix(n):
    solution = []
    print(f"Enter the {n} x 1 matrix by rows: ")
    for i in range(n):
        while True:
            row_list = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row_list) == 1:
                break
            else:
                print("Please enter a valid matrix.")
        solution.append(row_list)
    solution = np.array(solution, dtype=float)
    return solution


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
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

def random_matrix(n):
    return np.random.rand(n,n)

def random_solution_matrix(n):
    return np.random.rand(n)

def main():

    n = int(input("What is the size of the N x N matrix? "))
    choice = input("Do you want to enter a matrix(e) or create a random one(r)? (Enter 'e' or 'r') ")
    if choice == 'e':
        A = create_matrix(n)
        b = solution_matrix(n).flatten()
    else:
        A = random_matrix(n)
        b = random_solution_matrix(n)


    print(f"The System to be solved is: ")
    print("\nAugmented Matrix: \n{A |b}")
    print(np.hstack((A,b.reshape(-1, 1))))

    solution = gaussian_elimination(A,b)

    print("\nThe Solution Matrix is:")
    for i, val in enumerate(solution):
        print(f"Row {i+1}: {val:.4f}")
    c = np.linalg.solve(A,b)
    print("The python library to solve matrix is np.linalg.solve running this with the matrix results in: ")
    print(f"{c}")

if __name__ == "__main__":
    main()

"""
A = np.array([
    [2 -1 3 0 5 -2 4 1 -3],
    [4 2 -2 1 -3 5 0 6 7],
    [1 5 7 -2 4 -1 3 0 2],
    [3 0 -4 6 -1 2 5 -3 1],
    [5 7 2 -3 8 0 4 6 -2],
    [-2 4 1 3 -5 7 -6 0 8],
    [6 -3 5 0 2 4 1 -7 -1],
    [7 8 -2 4 -6 1 3 5 0],
    [-1 3 6 -5 0 2 7 -4 8]
])


b = np.array([10, 5, 8, 3, 7, 2, 6, 4, 9])
"""