s=set()
s.add(18)
s.add("18")
print(s)  # Output will be {18, '18'} since sets allow different types of elements

# but in case of double number it will not allow duplicates
s.add(18.0)  # This will not add a new element since 18 and 18.0 are considered the same in a set
print(s)  # Output will still be {18, '18'} since 18 and 18.0 are treated as the same element in a set

# What is the type of s={}? Its a dictionary, not a set