# The reduce function is the one that reduces an iterable to a single value by applying a binary function cumulatively.

from functools import reduce

# Find product of all numbers
nums = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, nums)
print(product)   # 120  (1*2*3*4*5)
