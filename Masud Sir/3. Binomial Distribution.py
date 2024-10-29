import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.5

x = np.arange(0, n + 1)
binom_probabilities = binom.pmf(x, n, p)

print("x values (number of successes):", x)
print("Binomial probabilities:", binom_probabilities)

plt.figure(figsize=(10, 6))
plt.bar(x, binom_probabilities, color='blue', alpha=0.7)
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.grid(True)
plt.show()



# Step 1: Import required libraries
# Import numpy for array handling, matplotlib for plotting, and scipy's binom function for binomial calculations

# Step 2: Define parameters for the Binomial distribution
# Set 'n' as the number of trials (e.g., flipping a coin 10 times)
# Set 'p' as the probability of success (e.g., 0.5 probability of getting heads)

# Step 3: Generate possible outcomes
# Use numpy's arange function to create an array 'x' that holds possible outcomes from 0 to 'n' successes

# Step 4: Calculate Binomial probabilities
# Use binom.pmf to compute the probability of each possible outcome in 'x' based on the parameters 'n' and 'p'
# This step yields an array of probabilities corresponding to each outcome in 'x'

# Step 5: Display results in text format
# Print the array of possible outcomes (x) and their corresponding probabilities for reference

# Step 6: Plot the Binomial distribution
# Use matplotlib to create a bar chart where each bar represents the probability of a given number of successes
# Customize the chart with labels for the x-axis (number of successes), y-axis (probability), and a title
# Add a grid to the plot to enhance readability and clarity of the distribution pattern

# Step 7: Show the plot
# Use plt.show() to display the final plot of the Binomial distribution


# A Binomial distribution models the number of successes in a fixed number of independent trials,
# where each trial has only two possible outcomes (success or failure) and each has the same probability of success.
# Example: flipping a coin multiple times and counting how many times it lands on heads