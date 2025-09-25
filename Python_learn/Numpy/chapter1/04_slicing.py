import numpy as np
# slicing in numpy
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original array:")
print(arr)
print("Sliced array:")
print(arr[1:3, 0:2])

# another way of slicing
print("Another way of slicing:")
print(arr[0:2, 1])
# slicing with the help of negative indexing
print("Slicing with negative indexing:")
print(arr[-2:, -3:-1])
# how it works is that it starts from the end of the array and goes backwards
# for the higher order array slicing rememnber the syntax is arr[x,y,z] where x is the first dimension, y is the second dimension and z is the third dimension

# step slicing
print("Step slicing:")
print(arr[::2, ::2])
# step slicing is used to skip elements in the array eg. if the step is 2 then it will skip every second element