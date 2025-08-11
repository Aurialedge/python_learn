x={1,2,3,"helllo"}
x.add(4)  # Adding an element to the set

# update method
x.update([5, 6, 7])  # Adding multiple elements to the set
print(x) # Output will be {1, 2, 3, 4, 5, 6, 7, 'helllo'}

# removing elements
x.remove(1)  # This will remove the element 1 from the set
# x.remove(10)  # This will raise a KeyError if 10 does not

# discarding the element
x.discard(2)  # This will remove the element 2 from the set if it exists
# x.discard(10)  # This will not raise an error if 10 does not exist

# ****************Properties of Sets****************
# Set is unordered, so the order of elements may change
# Set does not allow duplicates, so adding a duplicate element will not change the set
# set is unindexed, so you cannot access elements by index
# set is mutable, so you can add or remove elements
# There is no way to change an element in a set, you can only add or remove elements

# union and intersection
# union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_union = set1.union(set2)  # This will return a new set with elements from both sets

set_intersection = set1.intersection(set2)  # This will return a new set with common elements

# difference returns a new set with elements in set1 but not in set2
set_difference = set1.difference(set2)  # This will return a new set with

# symmetric difference returns a new set with elements in either set1 or set2 but not in both
set_symmetric_difference = set1.symmetric_difference(set2)  # This will return a new


# issubset and issuperset
# isdisjoint checks if two sets have no elements in common