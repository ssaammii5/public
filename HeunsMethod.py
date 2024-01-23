# Heun's Method (Euler's Modified Method)

import numpy as np
import matplotlib.pyplot as plt

x0 = 2
xn = 3
h = 0.2
y0 = 1

# dy/dx = f(x,y)
def f(x, y):
    return (4 - y**2) / (2 * x)

x = np.arange(x0, xn + h, h)
y = np.zeros_like(x)
yp = np.zeros_like(x)

y[0] = y0

for n in range(len(x) - 1):
    yp[n + 1] = y[n] + h * f(x[n], y[n])
    y[n + 1] = y[n] + (h / 2) * (f(x[n], y[n]) + f(x[n + 1], yp[n + 1]))

# exact = Integration of the function dy/dx
exact = 2 * (3 * x**2 - 4) / (3 * x**2 + 4)
abs_error = np.abs(exact - y)

print('--------------------------------------------------------------------------')
print('\tx\t\tApproximate\t\tExact\t\tAbs Error')
print('---------------------------------------------------------------------------')
for xi, yi, exact_i, error_i in zip(x, y, exact, abs_error):
    print(f'\t{xi:.1f}\t\t{yi:.6f}\t\t{exact_i:.6f}\t\t{error_i:.4e}')
print('---------------------------------------------------------------------------')

plt.plot(x, y, 'sr', label='Heuns Method')
plt.plot(x, exact, 'b', label='Exact')
plt.title('Heuns Method vs Exact Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
