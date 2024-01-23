import matplotlib.pyplot as plt
import numpy as np


def bisection(func, interval_range=1.0, tol=1e-6, max_iter=100):
    initial_guess = 0.0
    sign_change_found = False

    while initial_guess < 1e6:
        if func(initial_guess) * func(initial_guess + interval_range) <= 0:
            sign_change_found = True
            break
        initial_guess += interval_range

    if not sign_change_found:
        raise ValueError("Unable to find initial value")

    a = initial_guess
    b = initial_guess + interval_range

    print(f"Iteration\t a\t\t b\t\t\t c\t\t\t f(c)\t\t Percentage Error")

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {func(c):.6f}\t {100 * abs((c - a) / c):.6f}%")

        if func(c) == 0:
            return c, iteration + 1
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    root = (a + b) / 2
    print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {root:.6f}\t {func(root):.6f}\t {100 * abs((root - a) / root):.6f}%")
    return root, iteration


def target_function(x):
    return x ** 2 - 3


root, iterations = bisection(target_function)

print(f"\nRoot found: {root}")
print(f"Iterations: {iterations}")

# Plotting the function and bisection iterations
x_values = np.linspace(-2, 2, 1000)
y_values = target_function(x_values)

plt.plot(x_values, y_values, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)

# Highlighting the root
plt.scatter(root, 0, color='red', label='Root')

# Adding bisection iterations
plt.axvline(root, linestyle='--', color='green', label='Bisection iterations')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method')
plt.legend()
plt.grid(True)
plt.show()
