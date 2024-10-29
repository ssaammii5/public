import numpy as np
import matplotlib.pyplot as plt

# Parameters
Lambda = 1
num_samples = 10000  # Number of random samples to generate

# Define the inverse transform function for exponential distribution
def inverse_transform(X, Lambda):
    return -np.log(1 - X) / Lambda

# Generate random variates
output = [inverse_transform(np.random.rand(), Lambda) for _ in range(num_samples)]

# Calculate sample mean and variance
sample_mean = np.mean(output)
sample_variance = np.var(output)

# Calculate theoretical mean and variance
theoretical_mean = 1 / Lambda
theoretical_variance = 1 / (Lambda ** 2)

# Print the results in the specified format
print(f"Lambda = {Lambda}")
print(f"Sample Mean: {sample_mean:.4f}, Theoretical Mean: {theoretical_mean:.4f}")
print(f"Sample Variance: {sample_variance:.4f}, Theoretical Variance: {theoretical_variance:.4f}")

# Plotting the histogram of generated samples
plt.hist(output, bins=60, density=True, alpha=0.6, color='g')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Generated Samples from Inverse Transform Function')
plt.show()
