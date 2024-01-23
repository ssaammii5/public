import numpy as np
from scipy.integrate import quad

def f(x, y):
    return 1 + x * y

def picard_iteration(x_values, num_iterations):
    y_values = np.zeros(len(x_values))
    y_values[0] = 1  # Initial condition y(0) = 1

    for _ in range(num_iterations):
        for i in range(1, len(x_values)):
            integrand = lambda t: t * y_values[i - 1] + 1
            result, _ = quad(integrand, 0, x_values[i])
            y_values[i] = 1 + result

    return y_values

x_values = np.array([0.1, 0.2])

num_iterations = 2

y_values_approx = picard_iteration(x_values, num_iterations)

# Display the results
for i in range(len(x_values)):
    print(f'y({x_values[i]}) = {y_values_approx[i]}')
