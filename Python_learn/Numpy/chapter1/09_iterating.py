import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y) 
# another way of iterating us using nditer()
for x in np.nditer(arr):
    print(x)


# iterating with array of different data types
arr2=np.array([[1,2,3],[4,5,6]],dtype='S') # S means string
for x in np.nditer(arr2):
    print(x)
# we are iterating through the array and above we are printing the byte string so to convert it to string we can use the following method
for x in np.nditer(arr2, flags=['refs_ok']):
    print(x.astype(str))

# iterating with different step size
for x in np.nditer(arr2[::2]):
    print(x)


arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr1[:, ::2]):
  print(x)

# iterating with the ndenumerate() function
for idx, x in np.ndenumerate(arr):
    print(idx, x)
# here the idx is the index of the element and x is the value of the element