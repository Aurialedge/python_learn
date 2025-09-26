from numpy import random
arr=random.randint(100,size=(5))
print(arr)

# this is used to generate the random float number of size 5 eg. [0.123456 0.234567 0.345678 0.456789 0.567890]

# default type is float
# but we can also specify the type of the random number
# example
arr2=random.rand(5).astype(int)
print(arr2)

# generate the random number from 2 to 100
arr3=random.randint(2,100,size=(5))
print(arr3)

# the size attribute is used to specify the shape of the array
# example
arr4=random.rand(2,3)
print(arr4)
# it will generate the 2D array of shape 2x3

# choice function is used to generate the random number from the given array
arr5=random.choice([1,2,3,4,5],size=(3,4),p=[0.1,0.2,0.3,0.2,0.2])
print(arr5)
# choice function is used to generate the random number from the given array
