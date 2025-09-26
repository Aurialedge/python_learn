import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# for the search we have two functions
# 1. where()
# 2. searchsorted()


# using the where function
x=np.where(arr==5) # it will return the index of the element which is 5
print(x) # it will return a tuple of arrays (row_index, column_index)

# using the searchsorted function
arr1=np.array([1,2,3,4,5,6,7,8,9])
x1=np.searchsorted(arr1,5) # it will return the index where the element it will perform the binary search


print(x1) # it will return 4 because 5 is at index 4