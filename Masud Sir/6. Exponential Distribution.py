import numpy as np
Beta = 100  # Mean or Average
Lambda = [0.5, 1, 2, 4]  # Rate Parameter
X = 120
def exponential_distribution_with_beta(X, Beta):
    probability = 1 - np.exp(-X / Beta)
    # probability = (1 / Beta) * np.exp(-X / Beta)
    return probability


def exponential_distribution_with_lambda(X, Lambda):
    probability = 1 - np.exp(-X * Lambda)
    # probability = Lambda * np.exp(-Lambda * X)
    return probability
probability = exponential_distribution_with_beta(X, Beta)
print("When average = ", X, "it will take more than 120 days for the next wave to occur", (probability ),
      " % ")
p = exponential_distribution_with_lambda(X,(1/Beta))
print(p)

for lam in Lambda:
    probability = exponential_distribution_with_lambda(X, lam)
    print("When rate = ", lam, "It will take more than 120 days for the next wave to occur",
          probability, " % ")







# Importing the 'numpy' library for mathematical functions

# Setting initial parameters:
# 'Beta' is the mean or average time between events (e.g., 100 days).
# 'Lambda' is a list of rate parameters (e.g., [0.5, 1, 2, 4]) representing the occurrence rate of events per time unit.
# 'X' represents a specific time interval, here set to 120.

# Defining the exponential distribution:
# - An exponential distribution is a continuous probability distribution commonly used to model the time until an event occurs.
# - It describes the probability of waiting times between independent events that happen at a constant rate (e.g., time between earthquakes).
# - It is defined by either a rate parameter (Lambda) or a mean time parameter (Beta).
# - The exponential distribution has a "memoryless" property, meaning the probability of an event occurring in the future is independent of any past events.

# Defining the function 'exponential_distribution_with_beta':
# - This function calculates the probability using 'Beta' (mean time between events).
# - The formula used is 1 - exp(-X / Beta), giving the probability that the waiting time will exceed 'X' days.
# - An alternative formula for the probability density function (PDF) is commented out.

# Defining the function 'exponential_distribution_with_lambda':
# - This function calculates the probability using 'Lambda' (rate parameter).
# - The formula used is 1 - exp(-X * Lambda), giving the probability that the waiting time will exceed 'X' days.
# - An alternative PDF formula is also commented out.

# Calculating and printing the probability with 'Beta' as the average time:
# - The probability of taking more than 'X' days (120) until the next event is calculated and printed.

# Calculating and printing the probability with 'Lambda' as the rate parameter:
# - The rate 'Lambda' is calculated from 'Beta' using Lambda = 1 / Beta and used in the probability function.
# - Printing the resulting probability for the specified average.

# Iterating over multiple rate parameters in the 'Lambda' list:
# - For each Lambda value in the list, the probability of waiting more than 120 days until the next event is calculated.
# - Printing each result to show how the waiting probability varies with different rate parameters (Lambda).
