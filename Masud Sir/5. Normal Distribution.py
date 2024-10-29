import math
import numpy as np
import matplotlib.pyplot as plt


def normal_random_number(mean, deviation):
    return mean + deviation * np.random.randn()


rnn = []
mean = 100
standard_deviation = 20

for i in range(200):
    x = normal_random_number(mean, standard_deviation)
    rnn.append(x)

plt.hist(rnn, bins=20, density=True)

x = np.linspace(min(rnn), max(rnn), 200)
unimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(
    -((x - mean) ** 2) / (2 * standard_deviation ** 2))

# Plot the multimodal density curves
mean2 = 80
standard_deviation2 = 20
multimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(
    -((x - mean) ** 2) / (2 * standard_deviation ** 2)) + (1 / (standard_deviation2 * np.sqrt(2 * np.pi))) * np.exp(
    -((x - mean2) ** 2) / (2 * standard_deviation2 ** 2))

plt.plot(x, unimodal_curve, label='Unimodal', color='red')
plt.plot(x, multimodal_curve, label='Multimodal', color='black')
plt.show()



# Importing necessary libraries
# 'math' for mathematical constants and operations, 'numpy' for generating random numbers and mathematical functions,
# and 'matplotlib.pyplot' for plotting

# Defining a function 'normal_random_number' to generate a random number following a normal distribution
# Parameters:
# - 'mean' is the average value (center of the distribution)
# - 'deviation' is the standard deviation, controlling the spread around the mean
# Formula:
# - The function returns a random number by adding a random value from a standard normal distribution (mean=0, std=1) scaled by 'deviation' and shifted by 'mean'

# Normal Distribution overview:
# - A normal distribution is a continuous probability distribution characterized by its bell-shaped curve, also known as the Gaussian distribution.
# - It is symmetrical around the mean, where most values cluster around the center, and the probability tapers off symmetrically in both directions.
# - In this code, the normal distribution is used to simulate data points around a defined mean and standard deviation.

# Initializing variables:
# - 'rnn' is an empty list to store generated random numbers
# - 'mean' is set to 100 and 'standard_deviation' to 20, defining the center and spread of the distribution

# Generating 200 random numbers:
# - Using a loop to generate 200 random numbers with 'normal_random_number' and appending each to the list 'rnn'

# Plotting the histogram of generated random numbers:
# - 'plt.hist' creates a histogram to show the frequency distribution of random numbers in 20 bins, normalized to form a probability density

# Creating a smooth range of values for plotting probability density functions (PDFs):
# - 'x' is an array of 200 evenly spaced values between the minimum and maximum values in 'rnn', used as x-coordinates for the density curves

# Plotting the Unimodal Normal Curve:
# - Calculating the unimodal normal curve using the standard normal distribution formula
# - (1 / (σ * sqrt(2π))) * exp(-((x - μ)²) / (2σ²)), where μ = mean, σ = standard deviation
# - This curve represents a single peak centered around 'mean' and is plotted in red

# Defining parameters for a second normal distribution:
# - 'mean2' set to 80 and 'standard_deviation2' to 20, representing a second peak for the multimodal distribution

# Plotting the Multimodal Density Curve:
# - Calculating the combined probability density for both normal distributions to create a multimodal curve
# - Each component of the multimodal curve is generated using its mean and standard deviation, creating two peaks
# - The multimodal curve is plotted in black to show two peaks, representing data with more than one central tendency

# Showing the plot:
# - Displaying the histogram of random numbers, the unimodal curve, and the multimodal curve for visual comparison
