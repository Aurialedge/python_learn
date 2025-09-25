import sys as os
# print(os.path)
# print(os.version)
import numpy as np
# declaration of the array
arr=np.array([1,2,3,4,5]) 

# if we want to dynamically create an array
print("Enter the size of the array")
size = int(input())
arr = np.empty(size)
print("Enter the elements of the array")
for i in range(size):
    arr[i] = int(input())
print("The array is:")
print(arr)


#  checking the version op the numpy
print(np.__version__)

#  checking the type of the array
print(type(arr))
# output of above line is <class 'numpy.ndarray'> as this is the object of the numpy array
print(arr.dtype)
# output of above line is int32 which means 32 bit integer