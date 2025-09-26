import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
# I will show you how to spli the array
# there are three functions to split the array
# 1. array_split()
# 2. hsplit()
# 3. vsplit()

# array_split()
arr1=np.array_split(arr,2) # we are splitting the array into 2 parts
print(arr1)

# accessing the splitted array
print(arr1[0]) # first part of the splitted array
print(arr1[1]) # second part of the splitted array
# we can also split the array into more than 2 parts
arr2=np.array_split(arr,3) # we are splitting the array into 3 parts
print(arr2)


# hsplit() is just opposite of hstack()
arr3=np.hsplit(arr,3) # we are splitting the array into 3 parts

# vsplit() is just opposite of vstack()
arr4=np.vsplit(arr,2) # we are splitting the array into 2 parts
print(arr4)