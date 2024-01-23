# Newton-Raphson Method
import matplotlib.pyplot as plt



def f(x):
    return x ** 3 - x ** 2 - 2


def df(x):
    return 3 * x ** 2 - 2 * x


a = 1.5
n = 10
k = 1

# Lists to store iteration numbers and corresponding roots for plotting
iterations = []
roots = []

while k <= n:
    r = a - f(a) / df(a)
    print("Root:", r, "at Iteration", k)

    # Append values for plotting
    iterations.append(k)
    roots.append(r)

    k = k + 1
    a = r

# Plotting
plt.plot(iterations, roots, marker='o', linestyle='-')
plt.title('Convergence of Newton-Raphson Method')
plt.xlabel('Iteration')
plt.ylabel('Root')
plt.grid(True)
plt.show()
