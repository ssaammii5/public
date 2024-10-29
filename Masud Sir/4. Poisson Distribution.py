import math
import matplotlib.pyplot as plt
def poisson_distribution(lambd, x):
    # lambd = average_rate_of_event
    # x = number_of_event_occurring
    return (math.exp(-lambd) * (lambd ** x)) / math.factorial(x)
Lambda = [5, 10, 15]
for lam in Lambda:
    out = []
    for x in range(0, 11):
        out.append(poisson_distribution(lam, x))
    plt.plot(out)
    plt.xlabel("Time")
    plt.ylabel("Probability")
    plt.show()




# Importing necessary libraries
# Importing 'math' for mathematical operations and 'matplotlib.pyplot' for plotting

# Defining a function 'poisson_distribution' that calculates the Poisson probability for a given lambda and x
# Parameters:
# - 'lambd' represents the average rate of events (e.g., the expected number of events in a time period)
# - 'x' is the number of times the event actually occurs
# Formula:
# - Returns the Poisson probability using the formula:
#   (e^(-λ) * λ^x) / x!, where 'e' is the mathematical constant ~2.718

# Poisson distribution overview:
# - A Poisson distribution models the probability of a given number of events occurring within a fixed interval of time or space.
# - It assumes that events happen independently, with a constant average rate, and are rare in occurrence.
# - Example: predicting the number of emails received in an hour or the number of car accidents at an intersection per day

# Setting different values for lambda (5, 10, and 15) to observe how the distribution changes with different average rates of events

# Iterating over each lambda value
# - For each lambda, an empty list 'out' is created to store calculated probabilities for each possible x (from 0 to 10)

# Calculating and storing probabilities:
# - For each x value in the range (0 to 10), the Poisson probability is calculated and appended to 'out'

# Plotting the Poisson distribution:
# - For each lambda value, a line plot of the probability distribution is created and displayed
# - The x-axis represents the 'Time' or 'Number of Events', and the y-axis represents the 'Probability'
# - Showing each plot to visualize how probabilities change with different lambda values
