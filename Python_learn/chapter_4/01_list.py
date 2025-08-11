#  this is the information of the list that is used in the python

#  you can puth the values of different datatype in the list

x= [1, 2, 3, 4, 5, "Shivraj", 6.7, True]
print(x)  # Output: [1, 2, 3, 4, 5, 'Shivraj', 6.7, True]


#  Important

# String was immutable right 
# It means you cannot change the string but you can change the list

# eg.
z="shivraj"
# z[0] = "S" This will raise an error because strings are immutable


# But in the list you can change the value even if its string value
# eg.
y = ["shivraj", 1, 2, 3]
y[0] = "Shivraj"  # This will work because lists are mutable