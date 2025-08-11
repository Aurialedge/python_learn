# Write the program to showcase tuple is immutable
#  and how to use tuple method
x=(23.42, 45, "hi", 2.5, True)
print(x)
x[2] = "hello"  # This will raise a TypeError because tuples are immutable