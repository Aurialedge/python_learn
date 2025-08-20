# map function
# map function can be used to apply a function to all items in an iterable (e.g., list) and return a new iterable with the results.
# syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Keep only even numbers
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]
