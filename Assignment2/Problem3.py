import numpy as np



def create_matrix(n):
    matrix = []
    print(f"Enter the {n} x {n} matrix by rows: ")
    for i in range(n):
        while True:
            row_list = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row_list) == n:
                break
            else:
                print("Please enter a valid matrix.")
        matrix.append(row_list)
    matrix = np.array(matrix, dtype=float)
    return matrix


def crout(A):
    n = len(A)
    L = zero_matrix(n)
    U = identity_matrix(n)

    for i in range(n):
        #Lower Triangular Matrix L
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (L[i][k] * U[k][j])
            L[j][i] = A[j][i] - sum

        #Upper Triangle
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (L[i][k] * U[k][j])
            U[i][j] = (A[i][j] - sum)/ L[i][i]
    return L, U

def identity_matrix(n):
    I = np.identity(n)
    return I

def zero_matrix(n):
    Z = np.zeros((n,n))
    return Z

def main():

    n = int(input("What is the size of the N x N matrix? "))

    I = identity_matrix(n)
    Z = zero_matrix(n)

    
    A = create_matrix(n)
    print(f"The System to be solved is: ")
    print(f"\nMatrix: \n{A}")
    L,U = crout(A)
    print(f"\nLower Triangular Matrix: \n{L}")
    print(f"\nUpper Triangular Matrix: \n{U}")


if __name__ == "__main__":
    main()


# Test Cases
# # 3
# [[2, -1, 1],
# [-3, 3, 9],
# [-1, 2, 4]],