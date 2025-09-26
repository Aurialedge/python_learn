import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8,9])

# I will show how to filter the array we take the help of boolean indexing
x=arr1>5 # it will return a boolean array
print(x) # it will return [False False False False False  True  True  True  True]

# now I will show how to create the filtered array directly from the array is above method that I shown you 
arr2=arr1[x] # it will return the array which is greater than 5
print(arr2) # it will return [6 7 8 9]


arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)