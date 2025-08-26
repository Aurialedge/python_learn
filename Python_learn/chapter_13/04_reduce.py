# The reduce function is the one that reduces an iterable to a single value by applying a binary function cumulatively.

from functools import reduce

# Find product of all numbers
nums = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, nums)
print(product)   # 120  (1*2*3*4*5)

# more examples
# Find sum of all numbers
sum = reduce(lambda x, y: x + y, nums)
print(sum)      # 15   (1+2+3+4+5)

# Find maximum number
max_num = reduce(lambda x, y: x if x > y else y, nums)
print(max_num)  
# more examples
# Find minimum number
min_num = reduce(lambda x, y: x if x < y else y, nums)
print(min_num)  # 1

# complex example
# Find the product of all even numbers
even_product = reduce(lambda x, y: x * y if y % 2 == 0 else x, nums, 1)
print(even_product)  # 8 (2*4)