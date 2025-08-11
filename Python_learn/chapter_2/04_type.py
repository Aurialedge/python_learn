#  finding the type of a variable in python
#  using the type() function
x=23
print(type(x))  # This will print <class 'int'>

# typecasting in python
y=23.5
print(type(y))  # This will print <class 'float'>
y=int(y)  # converting float to int
print(type(y))  # This will print <class 'int'>

# the typecasting is valid only for some types or cases 
# for example, converting a string to an integer is valid only if the string contains a valid integer
z="123"
print(type(z))  # This will print <class 'str'>
z=int(z)  # converting string to int
print(type(z))  # This will print <class 'int'>

# eg if z="abc" it will give an error
# z=int(z)  # This will raise ValueError: invalid literal for int() with