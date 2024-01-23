import numpy as np
import sys


n = 3

a = np.array([
    [0.3, 0.52, 1, -0.01],
    [0.5, 1, 1.9, 0.67],
    [0.1, 0.3, 0.5, -0.44]
], dtype=float)


x = np.zeros(n)



# Applying GJ
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Ans
for i in range(n):
    x[i] = a[i][n] / a[i][i]

# Output
print('Solution: ')
for i in range(n):
    print(f"X{i} = {x[i]:.2f}",end="\t")