from numpy import random
# the random distribution is used to generate the random number that follow  on the probability density function
# use of the choice function
# the choice function is used to generate the random number from the given array


# **********problem 1**********
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

# The probability for the value to be 3 is set to be 0.1

# The probability for the value to be 5 is set to be 0.3

# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0


arr=random.choice([3,5,7,9],size=(100),p=[0.1,0.3,0.6,0.0])