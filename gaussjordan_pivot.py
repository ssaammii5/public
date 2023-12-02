import numpy as np

def gauss_jordan(A, B):
    M = np.column_stack((A, B))

    n = len(A)
    for k in range(n):
        pivot_row = np.argmax(np.abs(M[k:, k])) + k
        M[[k, pivot_row]] = M[[pivot_row, k]]

        M[k] = M[k] / M[k, k]
        for j in range(n):
            if j != k:
                M[j] -= M[j, k] * M[k]

    x = M[:, -1]
    return x


A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
B = np.array([7.85, -19.3, 71.4])
print(gauss_jordan(A, B))