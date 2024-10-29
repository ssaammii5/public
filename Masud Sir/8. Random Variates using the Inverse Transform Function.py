# Given the exponential CDF: F(x) = 1 - e^(-λx),
# The inverse CDF: F^(-1)(X) = Y = -ln(1 - X) / λ.

import numpy as np
import matplotlib.pyplot as plt

Lambda = 1
num_samples = 10000

def inverse_transform(X, Lambda):
    return -np.log(1 - X) / Lambda

output = [inverse_transform(np.random.rand(), Lambda) for _ in range(num_samples)]

sample_mean = np.mean(output)
sample_variance = np.var(output)

theoretical_mean = 1 / Lambda
theoretical_variance = 1 / (Lambda ** 2)

print(f"Lambda = {Lambda}")
print(f"Sample Mean: {sample_mean:.4f}, Theoretical Mean: {theoretical_mean:.4f}")
print(f"Sample Variance: {sample_variance:.4f}, Theoretical Variance: {theoretical_variance:.4f}")

plt.hist(output, bins=60, density=True, alpha=0.6, color='g')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Generated Samples from Inverse Transform Function')
plt.show()






# Importing necessary libraries
# numpy is used for performing mathematical calculations, generating random numbers, and working with arrays
# matplotlib is used to plot a histogram, which visually represents the distribution of generated samples

# Parameters for the exponential distribution
# Lambda: The rate parameter of the exponential distribution, determining the rate of decay
# - Here, Lambda is set to 1, which means the average interval between events is 1
# - A higher Lambda results in a quicker decay, concentrating values closer to zero
# - A lower Lambda spreads values out more, indicating a slower decay rate

# num_samples: Specifies the total number of random variates (samples) to generate
# - Setting num_samples to a high value (e.g., 10,000) produces a larger dataset
# - A larger sample size gives more reliable estimates for the sample mean and variance,
#   making them closer to the theoretical mean and variance for the exponential distribution

# Define the inverse transform function for an exponential distribution
# - This function takes a uniform random variable X (generated between 0 and 1) and the rate parameter Lambda
# - It returns a random variate that follows an exponential distribution using the inverse transform method
# - The formula for the inverse transform for an exponential distribution is: -log(1 - X) / Lambda
#   where:
#   - X is a random number between 0 and 1, generated uniformly
#   - Lambda is the rate parameter, influencing the scale of the distribution

# Generate random variates from the exponential distribution
# - For each sample, generate a uniform random number between 0 and 1 using np.random.rand()
# - Apply the inverse transform to generate an exponential random variate
# - Append each generated variate to the output list, creating an array of 10,000 samples following an exponential distribution

# Calculate the sample mean and variance of the generated samples
# - Sample mean: The average value of all generated samples, computed with np.mean()
# - Sample variance: The spread of the generated samples around the mean, calculated with np.var()
# - Calculating these sample statistics helps verify if the generated samples approximate the theoretical values

# Calculate theoretical mean and variance for the exponential distribution
# - Theoretical Mean for an exponential distribution is given by 1 / Lambda
#   - This represents the expected value (average) of the distribution
# - Theoretical Variance is given by 1 / (Lambda ** 2)
#   - This indicates the expected spread of values around the mean
# - These theoretical values serve as benchmarks to compare against the sample mean and variance

# Print the results in a formatted output
# - Display Lambda, sample mean, theoretical mean, sample variance, and theoretical variance for easy comparison
# - The closer the sample statistics are to the theoretical values, the more accurately the samples represent the exponential distribution

# Histogram of generated exponential random variates
# Shows probability density of values generated using inverse transform method
# Characteristic exponential decay: high frequency near zero, decreases as values increase
# Y-axis: Probability Density (normalized), X-axis: Value of variates
# 60 bins provide detail, showing smooth decay pattern typical of exponential distribution
# Title indicates data generation method: inverse transform function
