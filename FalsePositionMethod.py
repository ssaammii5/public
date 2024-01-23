import matplotlib.pyplot as plt

def f(x):
    return x ** 10 - 1

# a = initial guess(float), b = final guess(float), n = iteration(int)

a = 0
b = 1.3
n = 10

if f(a) * f(b) > 0:
    print("False Position Method Fails.")
else:
    print("Iteration\t a\t\t b\t\t\t c\t\t\t f(c)\t\t Percentage Error")
    print("--------------------------------------------------------------------")

    k = 1
    c_old = 0  # Initial value for c_old

    iterations = []
    errors = []

    while k <= n:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        f_c = f(c)

        if c_old != 0:
            percentage_error = abs((c - c_old) / c) * 100
        else:
            percentage_error = 0

        print(f"{k}\t\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f_c:.6f}\t {percentage_error:.6f}%")

        c_old = c
        k += 1

        iterations.append(k)
        errors.append(percentage_error)

    print(f"\nApproximate Root: {c}")

    # Plotting the convergence
    plt.plot(iterations, errors, marker='o')
    plt.title('Convergence of False Position Method')
    plt.xlabel('Iteration')
    plt.ylabel('Percentage Error')
    plt.grid(True)
    plt.show()
