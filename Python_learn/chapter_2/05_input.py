a=input("Enter the number 1: ")
b=input("Enter the number 2: ")

print("Number 1 is:", a)
print("Number 2 is:", b)

print(a + b)  # This will concatenate the strings, not add them as numbers
# Output = Number 1 is: 5
#         Number 2 is: 10   
#         510
#  String concatenation occurs

# toget sum do the type casting
a = int(a)
b = int(b)
print("Sum of the numbers is:", a + b)  # This will now add the numbers correctly
# Output = Sum of the numbers is: 15