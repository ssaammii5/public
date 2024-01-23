import sympy as sy
import matplotlib.pyplot as plt

# Define the function
f = lambda x: 2000.0 * sy.ln(140000.0 / (140000.0 - (2100.0 * x))) - 9.8 * x

# Integration parameters
a = 8
b = 30
n = 6

# Calculate integral using Simpson's 3/8 Rule
h = (b - a) / n
sum = 0
for k in range(1, n):
    t = a + k * h
    if (k % 3 == 0):
        sum += 2 * f(t)
    else:
        sum += 3 * f(t)
approx = ((3 * h) / 8) * (f(a) + f(b) + sum)

# Exact value of integration
x = sy.Symbol("x")
exact = sy.integrate(f(x), (x, a, b))

# Calculate error
error = abs(exact - approx)
percent_error = (error * 100) / exact

# Print results
print("Value of Integration (Simpson's 3/8 Rule):", approx)
print("Exact value:", exact)
print("Error:", error)
print("Percent error:", percent_error, "%")

# Visualization using matplotlib
x_vals = list(range(a, b + 1))  # Adjust for desired precision
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="f(x)")

for k in range(1, n):
    t = a + k * h
    plt.axvline(x=t, color='gray', linestyle='--')

plt.title("Visualization of Integration using Simpson's 3/8 Rule")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
