# Euler's Method

import numpy as np
import matplotlib.pyplot as plt

x0 = 0
xn = 4
h = 0.5
y0 = 1

# dy/dx = f(x,y)
def f(x, y):
    return -2*x**3+12*x**2-20*x+8

x = np.arange(x0, xn + h, h)
y = np.zeros_like(x)
y[0] = y0

#y_{n+1} = y_n + h * f(x_n,y_n)
for n in range(len(x) - 1):
    y[n + 1] = y[n] + h * f(x[n], y[n])

# exact = Integration of the function dy/dx
exact = -x**4/2 + 4*x**3 - 10*x**2 + 8*x
abs_error = np.abs(exact - y)

print('--------------------------------------------------------------------------')
print('\tx\t\tApproximate\t\tExact\t\tAbs Error')
print('---------------------------------------------------------------------------')
for xi, yi, exact_i, abs_error_i in zip(x, y, exact, abs_error):
    print(f'\t{xi:.1f}\t\t{yi:.6f}\t\t{exact_i:.6f}\t\t{abs_error_i:.4e}')
print('---------------------------------------------------------------------------')

plt.plot(x, y, 'sr', label='Euler')
plt.plot(x, exact, 'b', label='Exact')
plt.title('Euler Method vs Exact Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
