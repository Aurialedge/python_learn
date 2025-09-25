import numpy as np
# dimension opf the array
arr = np.array([[1,2,3],[4,5,6]])
print(" the dimension of the array is:", arr.ndim)
# ndim is used to find the dimension of the array
# shape is used to find the shape of the array
# difference between shape and ndim is that shape returns a tuple of the dimensions of the array while ndim returns an integer representing the number of dimensions
print(" the shape of the array is:", arr.shape)

# higher dimension array
arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]], ndmin=3)
# ndmin is used to specify the minimum number of dimensions of the array
print(" the dimension of the array is:", arr2.ndim)