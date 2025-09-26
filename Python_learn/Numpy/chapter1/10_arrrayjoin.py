import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr3=np.concatenate((arr1,arr2))
print(arr3)

# join using stack function
arr4=np.stack((arr1,arr2),axis=1)
print(arr4)
# here axis=1 means we are joining the arrays column wise if axis=0 then it will join row wise
arr5=np.stack((arr1,arr2),axis=0)
print(arr5)
# here axis=0 means we are joining the arrays row wise if axis=1 then it will join column wise

# stacking using hstack and vstack
arr6=np.hstack((arr1,arr2))
print(arr6)
# output will be same as concatenate function
arr7=np.vstack((arr1,arr2))
print(arr7)
# here vstack will stack the arrays vertically and hstack will stack the arrays horizontally
# we can also use dstack to stack the arrays depth wise
arr8=np.dstack((arr1,arr2))
print(arr8)
# its same like for the axis=2 in the stack function ass we are stacking the arrays depth wise