# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).
unique_numbers = set()  # Using a set to store unique numbers
for i in range(8):
    unique_numbers.add(int(input("Enter a number: ")))
print("Unique numbers are:", unique_numbers)