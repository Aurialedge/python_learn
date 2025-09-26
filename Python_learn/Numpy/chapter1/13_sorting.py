import numpy as np
arr=np.array([4,5,2,1,5,2,5,6,8,9,0])
# for sorting the array we have two functions
# 1. sort()
# 2. argsort()

# using the sort function
arr1=np.sort(arr) # it will sort the array in ascending order
# just give the copy of the array the original array will not be changed
# for reversing the order or sorting in descending order we can use the [::-1] slicing
arr2=arr1[::-1]

# when we sort the array of bigger dimension
arr3=np.array([[3,2,1],[6,5,4],[9,8,7]])
arr4=np.sort(arr3) # it will sort each row of the array