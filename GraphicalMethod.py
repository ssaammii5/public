import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients and constants for the two linear equations
# Equation 1: a1*x + b1*y = c1
# Equation 2: a2*x + b2*y = c2
a1, b1, c1 = 2, 3, 5
a2, b2, c2 = -1, 2, 2

# Create a range of x values
x_values = np.linspace(-10, 10, 100)

# Calculate corresponding y values for each equation
y1_values = (c1 - a1 * x_values) / b1
y2_values = (c2 - a2 * x_values) / b2

# Plot the equations
plt.plot(x_values, y1_values, label='2x + 3y = 5')
plt.plot(x_values, y2_values, label='-x + 2y = 2')

# Mark the intersection point (solution) if it exists
solution = np.linalg.solve([[a1, b1], [a2, b2]], [c1, c2])
plt.scatter(solution[0], solution[1], color='red', label='Intersection (Solution)')

# Add labels and legend
plt.title('System of Linear Equations')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Print the solution
print(f'The solution to the system of equations is: x = {solution[0]}, y = {solution[1]}')

# Show the plot
plt.show()
