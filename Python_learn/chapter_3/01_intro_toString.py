# String is immutable

# String slicing
s = "Hello, World!"
print(s[6,12]) # Output: World!

# Syntax s[Start:Stop:Step] Start position is inclusive, Stop position is exclusive
print(s[7:12])  # Output: World

# To move the line up or down press Alt + Up/Down Arrow

c=s[:]
print(c)  # Output: Hello, World!

k=s[:5]
print(k)  # Output: Hello
m=s[7:]# Output: World!

l="0123456789"
print(l[::2])  # Output: 02468 (every second character)