# higher dimension array
import numpy as np
arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]], ndmin=3)
# ndmin is used to specify the minimum number of dimensions of the array

# accessing elements in higher dimension array
print("The element at index [0,1,2] is:", arr2[0,1,2])

# accessing by the negative indexing in higher duimension array
print("The element at index [-1,-2,-3] is:", arr2[-1,-2,-3])
