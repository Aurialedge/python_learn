# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s={8, 7, 12, "Harry", (1, 2)}  # Using a tuple instead of a list since sets cannot contain mutable types like lists
# print(s)  # This will raise a TypeError since lists are mutable and cannot be added to a set