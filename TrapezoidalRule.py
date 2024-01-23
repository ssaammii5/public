## Trapezoidal Rule

import sympy as sy
import matplotlib.pyplot as plt
import numpy as np


f = lambda x: 2000.0*sy.ln(140000.0 / (140000.0 - (2100.0*x))) - 9.8*x

# lower: a(float), upper: b(float), number of strips: n(int)
a = 8
b = 30
n = 2

h = (b-a)/n
k = 1
sum = 0

for k in range(1, n):
    t = a + k * h
    sum += f(t)

approx = (h/2)*(f(a)+f(b)+2*sum)
print("Value of Integration: ", approx)

# Exact Value of Integration
x = sy.Symbol("x")
exact = sy.integrate(f(x), (x, a, b))
print("Exact value: ", exact)

error = abs(exact-approx)
print("Error: ", error)

print("Percent error: ", (error*100) / exact, "%")


#----------------------------------------------------

x = sy.Symbol('x')
f = 2000.0 * sy.log(140000.0 / (140000.0 - (2100.0*x))) - 9.8*x

# Generate data for plotting
x_vals = np.linspace(8, 30, 100)
y_vals = [f.subs(x, val) for val in x_vals]

# Plot the curve
plt.plot(x_vals, y_vals, label='Curve')
plt.title('Plot of the Given Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
