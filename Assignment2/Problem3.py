import numpy as np

def random_matrix(n):
    return np.random.randint(-10, 10, size=(n,n))


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
                sum += L[i][k] * U[k][j]
            L[j][i] = A[j][i] - sum

        #Upper Triangle
        for j in range(i+1, n):
            sum = 0
            for k in range(i):
                sum += (L[i][k] * U[k][j])
            if np.isclose(L[i][i],0):
                raise ValueError("Matrix is singular. No inverse exists.")
            U[i][j] = (A[i][j] - sum)/ L[i][i]
    return L, U

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] = y[i] / L[i][i]
    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] = x[i] / U[i][i]
    return x

def inverse_matrix(A):
    n = len(A)
    (L, U) = crout(A)
    I = identity_matrix(n)
    inv_A = np.zeros((n,n))

    for i in range(n):
        y = forward_substitution(L, I[:, i])
        x = backward_substitution(U, y)
        inv_A[:,i] = x
    return inv_A



def identity_matrix(n):
    return np.identity(n)

def zero_matrix(n):
    return np.zeros((n,n))

def main():
    n = int(input("What is the size of the N x N matrix? "))
    choice = input("Do you want to enter the matrix manually? (y/n): ")
    if choice == 'y':
        A = create_matrix(n)
    else:
        A = random_matrix(n)

    print(f"\nMatrix: \n{A}")
    try:
        L, U = crout(A)
        print(f"\nLower Triangular Matrix: \n{L}")
        print(f"\nUpper Triangular Matrix: \n{U}")
        #print(f"Python function verification: \n{np.dot(L, U)}")
        #compute inverse
        inv_A = inverse_matrix(A)
        print(f"\nInverse Matrix: \n{inv_A}")
        print(f"Python function verification: \n{np.linalg.inv(A)}")
        print(f"\nVerification: \n{np.round(np.dot(A, inv_A))}")
        print(f"\nVerification: \n{np.round(np.dot(inv_A, A))}")
        print(f"verification: \n{np.round(np.dot(A, np.linalg.inv(A)))}")
        print(f"\nVerification: \n{np.round(np.dot(np.linalg.inv(A), A))}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print("Matrix is singular. No inverse exists.")
        print(e)



if __name__ == "__main__":
    main()


# Test Cases
# # 3
# [[2, -1, 1],
# [-3, 3, 9],
# [-1, 2, 4]],