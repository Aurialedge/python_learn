import numpy as np
# we will dynamically enter the array and than dynamically reshape it
print("Enter the size of the array:")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        print(f"Enter element at position ({i},{j}): ", end="")
        element = int(input())
        if i == 0 and j == 0:
            arr = np.array([[element]])
        elif j == 0:
            arr = np.vstack([arr, [element]])
        else:
            arr[i] = np.append(arr[i], element)
        # here the vstack function is used to add a new row to the array and the append function is used to add a new element to the existing row
print("Original array:")
print(arr)
# reshaping the array
new_shape = (cols, rows)
reshaped_arr = arr.reshape(new_shape)
print("Reshaped array:")
print(reshaped_arr)

# unknown dimension
# for the unknown dimension we can use -1 and numpy will automatically calculate the dimension
reshaped_arr_unknown = arr.reshape(-1, rows)
print("Reshaped array with unknown dimension:")
print(reshaped_arr_unknown)