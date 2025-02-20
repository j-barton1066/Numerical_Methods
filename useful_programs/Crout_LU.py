"""
# Pseudocode for Crout Method

function crout_LU_decomposition(A):
    n = number of rows in A
    L = zero_matrix(n)
    U = identity_matrix(n)

    for j from 1 to n:
        # Lower Triangular Matrix L
        for i from j to n:
            sum = 0
            for k from 1 to j-1:
                sum = sum + (L[i][k] * U[k][j])
            L[i][j] = A[i][j] - sum

        # Upper Triangular Matrix U
        for i from j+1 to n:
            sum = 0
            for k from 1 to j-1:
                sum = sum + (L[j][k] * U[k][i])
            U[j][i] = (A[j][i] - sum) / L[j][j]

    return L, U

# Helper functions to create matrices
function identity_matrix(n):
    I = zero_matrix(n)
    for i from 1 to n:
        I[i][i] = 1
    return I

function zero_matrix(n):
    Z = matrix of n x n filled with zeros
    return Z

"""