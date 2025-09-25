import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
# making a copy of the array
arr2=arr.copy()
# view of the array
arr3=arr.view()
#  the difference between copy and view is that copy makes a new array and the original array remains unchanged while view makes a new array but the original array is affected if we change the view array

# checking if the array owns the data or not
#  we use the base attribute to check if the array owns the data or not
print("Does arr2 own the data?", arr2.base is None) # True because arr2 is a copy of arr and owns the data
print("Does arr3 own the data?", arr3.base is None) # False because arr3 is a view of arr and does not own the data