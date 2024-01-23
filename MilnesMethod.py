# Milne's Method

import numpy as np
import matplotlib.pyplot as plt

x0, xn, h, y0 = 0, 3, 0.5, 2

def f(x, y):
    return 0.5*(x+y)

x = np.arange(x0, xn + h, h)
y = np.zeros(len(x))
y[0] = y0

for n in range(3):
    k1 = h * f(x[n], y[n])
    k2 = h * f(x[n] + h/2, y[n] + k1/2)
    k3 = h * f(x[n] + h/2, y[n] + k2/2)
    k4 = h * f(x[n] + h, y[n] + k3)
    k = (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    y[n+1] = y[n] + k

yp = np.zeros_like(x)
for n in range(len(x) - 4):
    yp[n+4] = y[n] + (4*h/3) * (2*f(x[n+1], y[n+1]) - f(x[n+2], y[n+2]) + 2*f(x[n+3], y[n+3]))
    y[n+4] = y[n+2] + (h/3) * (f(x[n+2], y[n+2]) + 4*f(x[n+3], y[n+3]) + f(x[n+4], yp[n+4]))


print('--------------------------------------------------------------------------')
print('\tx\t\tApproximate(y)')
print('--------------------------------------------------------------------------')
for values in zip(x, y):
    print(f'\t{values[0]:.1f}\t\t{values[1]:.6f}')
print('--------------------------------------------------------------------------')



plt.plot(x, y, 'sr', label='Milnes')
plt.title('Milnes Method Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
