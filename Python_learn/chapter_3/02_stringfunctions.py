# This is the  string functions module

s="Shivraj"
print(len(s)) # Output:7

print(s.endswith("raj"))  # Output: True
print(s.startswith("hiv"))  # Output: False

# this are the case sensitive function it means 
# endswith Raj will return False
print(s.endswith("Raj"))  # Output: False

print(s.capitalize())  # Output: Shivraj (first letter capitalized)
print(s.upper())  # Output: SHIVRAJ (all letters uppercase)

m="This is a string"
print(m.title())  # Output: This Is A String (each word capitalized)


# Find and replace
print(m.find("is"))  # Output: 2 (index of first occurrence of "is")
print(m.replace("is", "was"))  # Output: Thwas was a string (replaces "is" with "was")