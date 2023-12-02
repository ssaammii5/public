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

    print(f"Iteration\t a\t\t b\t\t\t c\t\t\t f(c)")

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {func(c):.6f}")

        if func(c) == 0:
            return c, iteration + 1
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    root = (a + b) / 2
    print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {root:.6f}\t {func(root):.6f}")
    return root, iteration


def target_function(x):
    return x ** 2 - 3

root, iterations = bisection(target_function)

print(f"\nRoot found: {root}")
print(f"Iterations: {iterations}")