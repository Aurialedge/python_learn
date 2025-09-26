# here we have to learn about two functions
# 1. random.permutation
# 2. random.shuffle

# the shuffle function is used to shuffle the array
from numpy import random
arr=random.randint(100,size=(5))
print(arr)
random.shuffle(arr)
# the shuffle function is used to shuffle the array and get the random array in which indexing of the elements is not same as the original array
print(arr)

# generating the permutation of the array
arr2=random.permutation(arr)
print(arr2)
# the permutation formula is n!/(n-r)!
# but here we are not specifying the r value so it will take r as n
# so the permutation will be n!/(n-n)! = n!/0! = n!/1 = n!
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).

# np.random.permutation(x) → returns a new array (copy) with a random order.

# np.random.shuffle(x) → modifies x in-place and returns None. Use shuffle when you want to reorder an array without making a copy.


# so in short the shuffle function will change the original array but the permutation function will not change the original array it will return a new array with the permutation of the original array