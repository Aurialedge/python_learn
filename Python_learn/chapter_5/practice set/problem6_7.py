# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

favourite={
    "Shivraj": "Python",
    "Kurani": "Java",
}

# If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

# lets checkout
x={
    "Shivraj": "Python",
    "Shivraj": "Java",  # This will overwrite the previous value for "
}
print(x)  # Output will be {'Shivraj': 'Java'} since the second entry overwrites the first

# If languages of two friends are same; what will happen to the program in problem 
# 6? 

# lets checkout
y={
    "Shivraj": "Python",
    "Kurani": "Python",  # This will create a new key-value pair
}
print(y)  # Output will be {'Shivraj': 'Python', 'Kurani': 'Python'} since both keys are unique