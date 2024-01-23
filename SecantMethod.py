#Secant Method
import math
import matplotlib.pyplot as plt

f = lambda x: math.exp(-x) - x

def secant(f, x0, x1, M, delta, e):
    eapp = 0.0
    iterations = []
    errors = []

    print("Iteration\t xi-1\t\t txi\t\t xi+1\t\t\t E(approx)")

    for i in range(1, M):
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        if x2 != 0:
            eapp = abs((x2 - x1) / x2)
        iterations.append(i)
        errors.append(eapp)

        print(f"{i}\t\t\t {x0:.6f}\t {x1:.6f}\t {x2:.10f}\t {eapp:.10f}%")
        if abs(eapp) < delta or abs(f(x1)) < e:
            break
        else:
            x0 = x1
            x1 = x2

    print("Approximate Root: ", x2)

    # Plotting
    plt.plot(iterations, errors, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Error (approximation)')
    plt.title('Convergence of Secant Method')
    plt.show()

if __name__ == "__main__":
    secant(f, 0, 1, 1000, 10**-5, 19**-6)
