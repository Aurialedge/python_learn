#  Detecting the double space in the string
# This program checks for double spaces in a string and replaces them with a single space

k=input("Enter a string: ")

print(k.find("  "))  # Output: Index of the first occurrence of double space or -1 if not found

if k.find("  ") != -1:
    print("Double space found at index:", k.find("  "))  # Output: Index of double space