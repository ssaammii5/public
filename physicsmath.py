import numpy as np


m1 = 2.0
m2 = 3.0
m3 = 2.5
k = 10.0


g = 9.81


A = np.array([[k, -k, 0],
              [-k, k + k, -k],
              [0, -k, k + k]])
b = np.array([-m1 * g, -m2 * g, -m3 * g])


x = np.linalg.solve(A, b)


print("Displacement of mass 1:", x[0], "m")
print("Displacement of mass 2:", x[1], "m")
print("Displacement of mass 3:", x[2], "m")