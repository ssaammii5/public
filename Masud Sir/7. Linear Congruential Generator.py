r = [1]
a = 13
b = 1
m = 97
i = 1
ui = []

while i <= 10:
    rn = ((a*r[i-1])+b) % m
    r.append(rn)
    i+=1
    ui.append(rn/m)

uix = [(round(i, 2)) for i in ui]
print(r)
print(uix)







# Initializing variables:
# 'r' is a list with an initial seed value of 1, which is used to generate a sequence of random numbers.
# 'a', 'b', and 'm' are constants used in the linear congruential generator (LCG) formula:
# - 'a' is the multiplier, 'b' is the increment, and 'm' is the modulus.
# - These values control the randomness and periodicity of the generated sequence.
# 'i' is a counter starting from 1, and 'ui' is an empty list to store normalized values.

# Explanation of Linear Congruential Generator (LCG):
# - An LCG is a pseudorandom number generator that produces a sequence of numbers based on a recursive formula:
#   r(n) = (a * r(n-1) + b) % m
# - It is commonly used for generating pseudo-random numbers with a specified range and periodicity.
# - The generated numbers are deterministic, meaning the same seed produces the same sequence.

# Entering a loop to generate 10 random numbers using the LCG method:
# - 'rn' is calculated using the LCG formula with the previous value in the list 'r'.
# - 'rn' is then appended to the list 'r' to generate the next number in the sequence.
# - The normalized value of 'rn' (rn / m) is appended to 'ui' for each iteration to produce a value between 0 and 1.
# - 'i' is incremented to continue the loop until 10 values are generated.

# Rounding the generated 'ui' values to two decimal places:
# - Using list comprehension to round each value in 'ui' to two decimal places and store it in 'uix'

# Printing results:
# - 'r' contains the sequence of generated random numbers.
# - 'uix' contains the normalized and rounded values of 'r' as floating-point numbers between 0 and 1.
