#  using tuple methods

a=(1, 2, 3, 4, 5, 2)
no=a.count(2)  # counts the number of occurrences of 2 in the tuple
print(no)

# using the index method to find the index of the first occurrence of an element
index_of_2 = a.index(2)  # finds the index of the first occurrence of 2
print(index_of_2)

# If value is not present in the tuple, it will raise a ValueError
#  Optionally, you can specify a start and end index
# index_of_2 = a.index(2, 1, 4)  # finds the index of 2 between index 1 and 4


# Printing the tuple n times

new_tuple= a * 3  # repeats the tuple 3 times
print(new_tuple)

# checcking if the element is present in the tuple
is_present = 3 in a  # checks if 3 is in the tuple

# slicing of the tuple is similar to list only the tuple is immutable and value is returned