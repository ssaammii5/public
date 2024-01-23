import sympy as sy

x = sy.symbols('x')
y = sy.Function('y')

# Given differential equation
#here dy/dx = diff_eq =
diff_eq = -2*x**3+12*x**2-20*x+8

# Integrate the differential equation
solution = sy.integrate(diff_eq, x)

print("The solution to the differential equation(Integration):")
print(solution)
