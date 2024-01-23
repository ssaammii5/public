import numpy as np

def gausseliminate_with_pivot(A, b):
    n = len(b)

    aug = np.column_stack((A, b))

    for i in range(n):

        pivot_row = np.argmax(np.abs(aug[i:, i])) + i

        aug[[i, pivot_row]] = aug[[pivot_row, i]]

        aug[i] = aug[i] / aug[i, i]

        for j in range(i + 1, n):
            aug[j] -= aug[j, i] * aug[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = aug[i, -1] - np.dot(aug[i, i+1:n], x[i+1:])

    return x


A = np.array([[0.3, 0.52, 1],
              [0.5, 1, 1.9],
              [0.1, 0.3, 0.5]])

b = np.array([-0.01, 0.67, -0.44])

solution = gausseliminate_with_pivot(A, b)
print("Solution:", solution)



# Substituing With original equation

eq1 = np.allclose(np.dot(A[0, :], solution), b[0])
eq2 = np.allclose(np.dot(A[1, :], solution), b[1])
eq3 = np.allclose(np.dot(A[2, :], solution), b[2])

# Checking if all equations are satisfied
if eq1 and eq2 and eq3:
    print("The solution satisfies the system of equations.")
else:
    print("The solution does not satisfy the system of equations.")

