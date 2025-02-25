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

# def solution_matrix(n):
#     solution = []
#     print(f"Enter the {n} x 1 matrix by rows: ")
#     for i in range(n):
#         while True:
#             row_list = list(map(int, input(f"Row {i+1}: ").split()))
#             if len(row_list) == 1:
#                 break
#             else:
#                 print("Please enter a valid matrix.")
#         solution.append(row_list)
#     solution = np.array(solution, dtype=float)
#     return solution



def crout(A):
    n = len(A)
    L = zero_matrix(n)
    U = identity_matrix(n)

    for i in range(n):
        #Lower Triangular Matrix L
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum = sum + (L[i][k] * U[k][j])
        #Upper Triangle
        for j in range(i+1, n):
            sum = 0
            for k in range(i):
                sum = sum + (L[i][k] * U[k][j])
            U[i][j] = (A[i][j] - sum)
    return L, U

def identity_matrix(n):
    I = [[0] * n for _ in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I

def zero_matrix(n):
    Z = [[0] for _ in range(n)]
    return Z

def main():

    n = int(input("What is the size of the N x N matrix? "))

    I = identity_matrix(n)
    Z = zero_matrix(n)

    #
    # A = create_matrix(n)
    # print(f"The System to be solved is: ")
    print(f"\nMatrix: \n{I}")
    print(f"\nMatrix: \n{Z}")
    #
    #
    # crout = crout(A)
    #
    # print(crout)

if __name__ == "__main__":
    main()