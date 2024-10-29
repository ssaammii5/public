import numpy as np
import matplotlib.pyplot as plt

p = 0.6
n_trials = 1000

results = np.random.binomial(1, p, n_trials)

successes = np.sum(results)
failures = n_trials - successes

output = {
    "Number of trials": n_trials,
    "Probability of Success (p)": p,
    "Successes (1)": successes,
    "Failures (0)": failures
}

labels = ['Failure (0)', 'Success (1)']
counts = [failures, successes]

plt.bar(labels, counts, color=['blue', 'green'])
plt.title(f'Bernoulli Distribution (p = {p})')
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.show()

print(output)


# Import necessary libraries for numerical operations and plotting
# Set probability of success (p) and total number of Bernoulli trials
# Generate random samples from a Bernoulli distribution with given probability and trials

# The Bernoulli distribution is a discrete probability distribution that has only two possible outcomes:
# success (1) with probability p, and failure (0) with probability 1 - p.
# Each trial is independent, meaning the outcome of one trial does not affect the others.

# Calculate the total number of successful outcomes (1s)
# Calculate the total number of failed outcomes (0s)
# Store results in a dictionary with trial count, probability, successes, and failures
# Define labels for outcomes and their respective counts for plotting
# Create a bar chart showing the frequency of each outcome (success and failure)
# Add title and labels to the plot for clarity
# Display the bar plot
# Print the output dictionary showing the summary of trials, probability, successes, and failures
