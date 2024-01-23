#f(x) to f'(x)
from sympy import symbols, diff


# Define the variable
x = symbols('x')

# Define the function f(x)
f_x = x**3 - x**2 - 2

# Find the derivative of f(x) with respect to x
df_x = diff(f_x, x)

# Print the derivative
print("Derivative of f(x):", df_x)
